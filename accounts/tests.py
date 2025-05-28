from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile

class ProfileModelTest(TestCase):

    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username='newuser', password='testpass')
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_profile_str(self):
        user = User.objects.create_user(username='profileuser', password='testpass')
        profile = user.profile  # Access the one-to-one related object
        self.assertEqual(str(profile), "profileuser Profile")
