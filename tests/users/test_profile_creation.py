from django.contrib.auth import get_user_model
from django.test import TestCase


class ProfileModelTests(TestCase):
    """RS: this tests Django user profile one-to-one link. When a user is created,
    automatically their profile is created."""

    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create()

    def test_profile(self):
        profile = get_user_model().objects.last().profile
