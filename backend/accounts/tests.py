from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import CustomerProfile

User = get_user_model()


class RegisterAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_creates_profile(self):
        url = reverse("auth-register")
        payload = {
            "username": "newuser",
            "email": "new@test.com",
            "password": "longpassword1",
            "first_name": "N",
            "last_name": "U",
        }
        r = self.client.post(url, payload, format="json")
        self.assertEqual(r.status_code, 201)
        user = User.objects.get(username="newuser")
        self.assertTrue(user.check_password("longpassword1"))
        self.assertTrue(CustomerProfile.objects.filter(user=user).exists())
