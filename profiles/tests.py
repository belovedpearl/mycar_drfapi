from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_create_profile_signal(self):
        # Create a new user
        new_user = User.objects.create_user(
            username='ade',
            password='ola123'
        )
        # Check that a profile was created for the new user
        self.assertTrue(Profile.objects.filter(owner=new_user).exists())
