from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import InsurancePolicy

User = get_user_model()


class PortalAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="pass12345!!")
        InsurancePolicy.objects.create(
            user=self.user,
            policy_number="P-1",
            product_name="Kasko",
            premium_amount=Decimal("100.00"),
            start_date=date.today(),
            end_date=date.today(),
        )
        self.client = APIClient()

    def test_policies_requires_auth(self):
        url = reverse("me-policies")
        r = self.client.get(url)
        self.assertEqual(r.status_code, 401)

    def test_policies_returns_user_rows(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        url = reverse("me-policies")
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data), 1)
        self.assertEqual(r.data[0]["policy_number"], "P-1")
