from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from blog.models import Post

USER_MODEL = get_user_model()


class TestEditPostView(TestCase):
    """
    RS: test if non-logged-in users are redirected. 301 is status for redirection,
    which means the get request should have a response that is status 301.
    """

    user = None
    post_id = Post.objects.all().get(id=36)

    @classmethod
    def setUpTestData(cls):
        cls.user = USER_MODEL.objects.create_user(
            username='user123',
            password='password456'
        )
        cls.hacker = USER_MODEL.objects.create_user(
            username='hacker',
            password='password456'
        )
        cls.post = Post.objects.create(
            title='my title',
            author=cls.user,
            content='post content',
        )
        cls.client = Client()
        cls.url = '/blog/post/36/update'

    def test_user_must_be_logged_in(self):
        """ Tests that a non-logged in user is redirected """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 301)

    def test_non_authors_get_301(self):
        """ Tests that a logged-in user who is not the author gets a 301 """

        self.client.force_login(self.hacker)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 301)
