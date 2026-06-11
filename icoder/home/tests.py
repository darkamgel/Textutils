from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import Client, TestCase
from django.urls import reverse
from django.utils.timezone import now

from blog.models import Post
from home.models import Contact


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


class ContactModelTestCase(TestCase):
    def test_str_representation(self):
        contact = Contact.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            phone="1234567890",
            content="Hello there",
        )
        self.assertEqual(str(contact), "Message by Jane Doe - jane@example.com")

    def test_contact_fields_persist(self):
        contact = Contact.objects.create(
            name="John",
            email="john@example.com",
            phone="9876543210",
            content="Test message",
        )
        self.assertEqual(contact.name, "John")
        self.assertEqual(contact.email, "john@example.com")
        self.assertEqual(contact.phone, "9876543210")
        self.assertEqual(contact.content, "Test message")
        self.assertIsNotNone(contact.timeStamp)


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_returns_200(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")


class AboutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about_page_returns_200(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/about.html")


class ContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_get_returns_200(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/contact.html")

    def test_contact_post_valid_saves_message(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Alice",
                "email": "alice@example.com",
                "phone": "1234567890",
                "content": "This is a valid message",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your message has been successfully sent")

    def test_contact_post_invalid_does_not_save(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "A",
                "email": "ab",
                "phone": "123",
                "content": "Hi",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Please fill the form correctly")


class SearchViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        create_post(
            title="Django Tutorial",
            content="Learn Django basics",
            author="Coder",
            slug="django-tutorial",
        )

    def test_search_finds_post_by_title(self):
        response = self.client.get(reverse("search"), {"query": "Django"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/search.html")
        self.assertEqual(response.context["allPosts"].count(), 1)
        self.assertEqual(response.context["query"], "Django")

    def test_search_no_results_shows_warning(self):
        response = self.client.get(reverse("search"), {"query": "nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["allPosts"].count(), 0)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "No search results found. Please refine your query.",
        )

    def test_search_long_query_returns_empty(self):
        response = self.client.get(reverse("search"), {"query": "x" * 79})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["allPosts"].count(), 0)


class HandleSignUpTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_data = {
            "username": "testuser1",
            "email": "test@example.com",
            "fname": "Test",
            "lname": "User",
            "pass1": "securepass123",
            "pass2": "securepass123",
        }

    def test_signup_get_returns_not_found_message(self):
        response = self.client.get(reverse("handleSignUp"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "404 - Not found")

    def test_signup_valid_creates_user(self):
        response = self.client.post(reverse("handleSignUp"), self.valid_data)
        self.assertRedirects(response, reverse("home"))
        user = User.objects.get(username="testuser1")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")

    def test_signup_username_too_long(self):
        data = {**self.valid_data, "username": "a" * 11}
        response = self.client.post(reverse("handleSignUp"), data)
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(User.objects.filter(username="a" * 11).exists())

    def test_signup_username_not_alphanumeric(self):
        data = {**self.valid_data, "username": "user@name"}
        response = self.client.post(reverse("handleSignUp"), data)
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(User.objects.filter(username="user@name").exists())

    def test_signup_password_mismatch(self):
        data = {**self.valid_data, "pass2": "differentpass"}
        response = self.client.post(reverse("handleSignUp"), data)
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(User.objects.filter(username="testuser1").exists())


class HandleLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="loginuser",
            email="login@example.com",
            password="testpass123",
        )

    def test_login_get_returns_not_found_message(self):
        response = self.client.get(reverse("handleLogin"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "404 - Not found")

    def test_login_valid_credentials(self):
        response = self.client.post(
            reverse("handleLogin"),
            {"loginusername": "loginuser", "loginpassword": "testpass123"},
        )
        self.assertRedirects(response, reverse("home"))

    def test_login_invalid_credentials(self):
        response = self.client.post(
            reverse("handleLogin"),
            {"loginusername": "loginuser", "loginpassword": "wrongpassword"},
        )
        self.assertRedirects(response, reverse("home"))


class HandleLogoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="logoutuser",
            email="logout@example.com",
            password="testpass123",
        )

    def test_logout_redirects_to_home(self):
        self.client.login(username="logoutuser", password="testpass123")
        response = self.client.get(reverse("handleLogout"))
        self.assertRedirects(response, reverse("home"))
