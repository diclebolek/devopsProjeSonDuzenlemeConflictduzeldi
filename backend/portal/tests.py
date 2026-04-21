from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import ClaimTicket, CustomerAlert, InsurancePolicy, InsuranceQuote, PaymentNotice

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
        InsuranceQuote.objects.create(
            user=self.user,
            reference_code="Q-1",
            product_type="Trafik",
            offered_premium=Decimal("200.00"),
        )
        ClaimTicket.objects.create(
            user=self.user,
            claim_number="C-1",
            incident_date=date.today(),
        )
        PaymentNotice.objects.create(
            user=self.user,
            due_date=date.today(),
            amount=Decimal("50.00"),
        )
        CustomerAlert.objects.create(user=self.user, title="Test")
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

    def test_other_user_data_not_visible(self):
        user2 = User.objects.create_user(username="u2", password="pass12345!!")
        InsurancePolicy.objects.create(
            user=user2,
            policy_number="P-2",
            product_name="Trafik",
            premium_amount=Decimal("100.00"),
            start_date=date.today(),
            end_date=date.today(),
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        r = self.client.get(reverse("me-policies"))
        policy_numbers = [item["policy_number"] for item in r.data]
        self.assertIn("P-1", policy_numbers)
        self.assertNotIn("P-2", policy_numbers)

    def test_all_private_lists_return_200(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        self.assertEqual(self.client.get(reverse("me-quotes")).status_code, 200)
        self.assertEqual(self.client.get(reverse("me-claims")).status_code, 200)
        self.assertEqual(self.client.get(reverse("me-payments")).status_code, 200)
        self.assertEqual(self.client.get(reverse("me-alerts")).status_code, 200)
