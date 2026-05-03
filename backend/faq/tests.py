from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import FAQEntry


class FAQAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        FAQEntry.objects.create(question="S1", answer="A1", is_active=True, sort_order=1)
        FAQEntry.objects.create(question="S2", answer="A2", is_active=False, sort_order=2)

    def test_faq_list_returns_only_active(self):
        r = self.client.get(reverse("faq-list"))
        self.assertEqual(r.status_code, 200)
        questions = [item["question"] for item in r.data]
        self.assertIn("S1", questions)
        self.assertNotIn("S2", questions)

    def test_faq_list_status_code(self):
        r = self.client.get(reverse("faq-list"))
        self.assertEqual(r.status_code, 200)


class FAQModelTests(TestCase):
    def test_ordering_by_sort_order_then_id(self):
        FAQEntry.objects.create(question="Q2", answer="A2", is_active=True, sort_order=2)
        FAQEntry.objects.create(question="Q1", answer="A1", is_active=True, sort_order=1)
        items = list(FAQEntry.objects.all())
        self.assertEqual(items[0].question, "Q1")
