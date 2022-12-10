from blog.models import Post
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
USER_MODEL = get_user_model()


class TestPostModel(TestCase):
    """
    Things to test:
    - Can a post be created with the required fields? (title, content and author)
    - Does the __str__ method behave as expected?
    """

    user = None

    @classmethod
    def setUpTestData(cls):
        cls.user = USER_MODEL.objects.create_user(
            username='user123',
            password='password456'
        )

        cls.post = Post.objects.create(
            title='My blog post',
            content='This is my first post',
            author=cls.user,
        )

    def test_create_post(self):
        """ Tests that a post with a title, content, and author can be created"""

        self.assertEqual(self.post.title, 'My blog post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.content, 'This is my first post')

    def test_post_str(self):
        """ Tests the __str__ of the Post model"""

        self.assertEqual(str(self.post), 'My blog post')

