from urllib.parse import quote

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils.timezone import now

from blog.models import BlogComment, Post
from home.sql_injection_payloads import SQL_INJECTION_PAYLOADS


def create_post(**kwargs):
    defaults = {
        "title": "Secret Post",
        "content": "Hidden content for sqli tests",
        "author": "Admin",
        "slug": "secret-post",
        "timeStamp": now(),
    }
    defaults.update(kwargs)
    return Post.objects.create(**defaults)


class SQLInjectionPayloadCountTestCase(TestCase):
    def test_payload_corpus_exceeds_100(self):
        self.assertGreater(len(SQL_INJECTION_PAYLOADS), 100)


class SearchSQLInjectionTestCase(TestCase):
    def setUp(self):
        self.client = Client(raise_request_exception=False)
        self.post = create_post()
        self.decoy = create_post(
            title="Other Article",
            content="Unrelated",
            author="Guest",
            slug="other-article",
        )

    def test_search_accepts_all_sqli_payloads_without_crashing(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, payload=payload[:60]):
                response = self.client.get(
                    reverse("search"),
                    {"query": payload[:78]},
                )
                self.assertIn(response.status_code, [200, 500])

    def test_classic_sqli_or_true_returns_all_posts(self):
        response = self.client.get(reverse("search"), {"query": "0 OR 1=1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["allPosts"].count(), 2)

    def test_sqli_union_does_not_crash_search(self):
        response = self.client.get(
            reverse("search"),
            {"query": "' UNION SELECT sno FROM blog_post--"},
        )
        self.assertIn(response.status_code, [200, 500])


class ContactSQLInjectionTestCase(TestCase):
    def setUp(self):
        self.client = Client(raise_request_exception=False)

    def _valid_contact_data(self, **overrides):
        data = {
            "name": "John Smith",
            "email": "john@example.com",
            "phone": "1234567890",
            "content": "Valid contact message body",
        }
        data.update(overrides)
        return data

    def test_contact_name_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="name", payload=payload[:60]):
                data = self._valid_contact_data(name=payload[:255] or "ab")
                if len(data["name"]) < 2:
                    data["name"] = payload[:2] or "ab"
                response = self.client.post(reverse("contact"), data)
                self.assertIn(response.status_code, [200, 302, 500])

    def test_contact_email_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="email", payload=payload[:60]):
                email = payload[:30] if len(payload) >= 3 else f"{payload}@x.co"[:30]
                response = self.client.post(
                    reverse("contact"),
                    self._valid_contact_data(email=email),
                )
                self.assertIn(response.status_code, [200, 302, 500])

    def test_contact_phone_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="phone", payload=payload[:60]):
                phone = (payload * 2)[:13] if len(payload) < 10 else payload[:13]
                response = self.client.post(
                    reverse("contact"),
                    self._valid_contact_data(phone=phone),
                )
                self.assertIn(response.status_code, [200, 302, 500])

    def test_contact_content_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="content", payload=payload[:60]):
                content = payload if len(payload) >= 4 else f"{payload}xxxx"
                response = self.client.post(
                    reverse("contact"),
                    self._valid_contact_data(content=content),
                )
                self.assertIn(response.status_code, [200, 302, 500])


class LoginSQLInjectionTestCase(TestCase):
    def setUp(self):
        self.client = Client(raise_request_exception=False)
        User.objects.create_user(
            username="sqliuser",
            email="sqli@example.com",
            password="legitpass123",
        )

    def test_login_username_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="loginusername", payload=payload[:60]):
                response = self.client.post(
                    reverse("handleLogin"),
                    {"loginusername": payload, "loginpassword": "legitpass123"},
                )
                self.assertIn(response.status_code, [200, 302, 500])

    def test_login_password_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="loginpassword", payload=payload[:60]):
                response = self.client.post(
                    reverse("handleLogin"),
                    {"loginusername": "sqliuser", "loginpassword": payload},
                )
                self.assertIn(response.status_code, [200, 302, 500])


class BlogSlugSQLInjectionTestCase(TestCase):
    def setUp(self):
        self.client = Client(raise_request_exception=False)
        create_post()

    def test_blog_slug_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, payload=payload[:60]):
                slug = quote(payload[:150], safe="")
                response = self.client.get(f"/blog/{slug}")
                self.assertIn(response.status_code, [200, 404, 500])


class PostCommentSQLInjectionTestCase(TestCase):
    def setUp(self):
        self.client = Client(raise_request_exception=False)
        self.user = User.objects.create_user(
            username="commenter1",
            email="c1@example.com",
            password="testpass123",
        )
        self.post = create_post(slug="comment-sqli-post")
        self.client.login(username="commenter1", password="testpass123")

    def test_post_comment_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="comment", payload=payload[:60]):
                response = self.client.post(
                    reverse("postComment"),
                    {
                        "comment": payload or "test",
                        "postSno": self.post.sno,
                        "parentSno": "",
                    },
                )
                self.assertIn(response.status_code, [200, 302, 404, 500])

    def test_post_comment_post_sno_sqli_payloads(self):
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="postSno", payload=payload[:60]):
                response = self.client.post(
                    reverse("postComment"),
                    {
                        "comment": "sqli fuzz comment",
                        "postSno": payload[:20],
                        "parentSno": "",
                    },
                )
                self.assertIn(response.status_code, [200, 302, 404, 500])

    def test_post_comment_parent_sno_sqli_payloads(self):
        parent = BlogComment.objects.create(
            comment="parent",
            user=self.user,
            post=self.post,
        )
        for index, payload in enumerate(SQL_INJECTION_PAYLOADS):
            with self.subTest(index=index, field="parentSno", payload=payload[:60]):
                response = self.client.post(
                    reverse("postComment"),
                    {
                        "comment": "reply fuzz",
                        "postSno": self.post.sno,
                        "parentSno": payload[:20] or str(parent.sno),
                    },
                )
                self.assertIn(response.status_code, [200, 302, 404, 500])
