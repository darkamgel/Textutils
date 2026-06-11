from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import Client, TestCase
from django.urls import reverse
from django.utils.timezone import now

from blog.models import BlogComment, Post
from blog.templatetags.extras import get_val


def create_post(**kwargs):
    defaults = {
        "title": "Test Post",
        "content": "Test content",
        "author": "Author",
        "slug": "test-post",
        "timeStamp": now(),
    }
    defaults.update(kwargs)
    return Post.objects.create(**defaults)


class PostModelTestCase(TestCase):
    def test_str_representation(self):
        post = create_post(
            title="My Post",
            content="Post content",
            author="Author",
            slug="my-post",
        )
        self.assertEqual(str(post), "My Post by Author")

    def test_post_fields_persist(self):
        post = create_post(
            title="Title",
            content="Content body",
            author="Writer",
            slug="title",
        )
        self.assertEqual(post.title, "Title")
        self.assertEqual(post.content, "Content body")
        self.assertEqual(post.author, "Writer")
        self.assertEqual(post.slug, "title")


class BlogCommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="commenter",
            email="commenter@example.com",
            password="testpass123",
        )
        self.post = create_post(
            title="Commented Post",
            content="Content",
            author="Author",
            slug="commented-post",
        )

    def test_str_representation(self):
        comment = BlogComment.objects.create(
            comment="This is a test comment",
            user=self.user,
            post=self.post,
        )
        self.assertEqual(str(comment), "This is a tes... by commenter")

    def test_comment_with_parent(self):
        parent = BlogComment.objects.create(
            comment="Parent comment",
            user=self.user,
            post=self.post,
        )
        reply = BlogComment.objects.create(
            comment="Reply comment",
            user=self.user,
            post=self.post,
            parent=parent,
        )
        self.assertEqual(reply.parent, parent)
        self.assertEqual(parent.blogcomment_set.count(), 1)


class BlogHomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = create_post(
            title="Blog Home Post",
            content="Visible on blog home",
            author="Blogger",
            slug="blog-home-post",
        )

    def test_blog_home_returns_200(self):
        response = self.client.get(reverse("bloghome"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blogHome.html")

    def test_blog_home_lists_all_posts(self):
        response = self.client.get(reverse("bloghome"))
        self.assertIn(self.post, response.context["allPosts"])


class BlogPostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="blogger",
            email="blogger@example.com",
            password="testpass123",
        )
        self.post = create_post(
            title="Single Post",
            content="Full post content",
            author="Author",
            slug="single-post",
        )
        self.parent_comment = BlogComment.objects.create(
            comment="Top level comment",
            user=self.user,
            post=self.post,
        )
        self.reply = BlogComment.objects.create(
            comment="Nested reply",
            user=self.user,
            post=self.post,
            parent=self.parent_comment,
        )

    def test_blog_post_returns_200(self):
        response = self.client.get(
            reverse("blogPost", kwargs={"slug": self.post.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blogPost.html")
        self.assertEqual(response.context["post"], self.post)

    def test_blog_post_includes_comments_and_replies(self):
        response = self.client.get(
            reverse("blogPost", kwargs={"slug": self.post.slug})
        )
        self.assertIn(self.parent_comment, response.context["comments"])
        self.assertIn(
            self.reply,
            response.context["replyDict"][self.parent_comment.sno],
        )


class PostCommentViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="poster",
            email="poster@example.com",
            password="testpass123",
        )
        self.post = create_post(
            title="Comment Target",
            content="Post for comments",
            author="Author",
            slug="comment-target",
        )
        self.client.login(username="poster", password="testpass123")

    def test_post_comment_creates_top_level_comment(self):
        response = self.client.post(
            reverse("postComment"),
            {
                "comment": "A new comment",
                "postSno": self.post.sno,
                "parentSno": "",
            },
        )
        self.assertRedirects(response, f"/blog/{self.post.slug}")
        self.assertEqual(BlogComment.objects.count(), 1)
        comment = BlogComment.objects.first()
        self.assertEqual(comment.comment, "A new comment")
        self.assertEqual(comment.user, self.user)
        self.assertIsNone(comment.parent)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "thank you for comment.")

    def test_post_comment_creates_reply(self):
        parent = BlogComment.objects.create(
            comment="Parent",
            user=self.user,
            post=self.post,
        )
        response = self.client.post(
            reverse("postComment"),
            {
                "comment": "A reply",
                "postSno": self.post.sno,
                "parentSno": parent.sno,
            },
        )
        self.assertRedirects(response, f"/blog/{self.post.slug}")
        reply = BlogComment.objects.get(comment="A reply")
        self.assertEqual(reply.parent, parent)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "thank you for reply.")


class ExtrasTemplateTagTestCase(TestCase):
    def test_get_val_returns_value_for_existing_key(self):
        data = {"foo": "bar"}
        self.assertEqual(get_val(data, "foo"), "bar")

    def test_get_val_returns_none_for_missing_key(self):
        data = {"foo": "bar"}
        self.assertIsNone(get_val(data, "missing"))
