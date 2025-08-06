from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.profile.full_name = 'Test User'
        self.user.profile.phone_number = '+911234567890'
        self.user.profile.save()

    def test_profile_created(self):
        """Test that the user profile is created automatically."""
        profile = self.user.profile
        self.assertEqual(profile.full_name, 'Test User')
        self.assertEqual(profile.phone_number, '+911234567890')
        self.assertEqual(profile.user.username, 'testuser')