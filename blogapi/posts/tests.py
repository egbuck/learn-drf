from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email="test@email.com",
            password='testpassword',
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='Test Post',
            body='This is a test post.',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.body, "This is a test post.")
        self.assertEqual(str(self.post), "Test Post")