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

    def test_register_rejects_short_password(self):
        url = reverse("auth-register")
        payload = {
            "username": "weakuser",
            "email": "weak@test.com",
            "password": "123",
        }
        r = self.client.post(url, payload, format="json")
        self.assertEqual(r.status_code, 400)

    def test_login_returns_token_pair(self):
        User.objects.create_user(username="loginuser", password="longpassword1")
        url = reverse("token_obtain_pair")
        r = self.client.post(
            url,
            {"username": "loginuser", "password": "longpassword1"},
            format="json",
        )
        self.assertEqual(r.status_code, 200)
        self.assertIn("access", r.data)
        self.assertIn("refresh", r.data)


class AccountsModelTests(TestCase):
    def test_customer_profile_str(self):
        user = User.objects.create_user(username="profileuser", password="longpassword1")
        profile = CustomerProfile.objects.create(user=user)
        self.assertIn("profileuser", str(profile))
