from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Service, ServiceCategory


class ServiceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        cat = ServiceCategory.objects.create(name="Test", slug="test-cat")
        Service.objects.create(
            category=cat,
            title="Trafik",
            slug="trafik",
            short_description="Kısa",
            body="Uzun",
            is_published=True,
        )

    def test_list_returns_published_service(self):
        url = reverse("service-list")
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data), 1)
        self.assertEqual(r.data[0]["slug"], "trafik")

    def test_detail_by_slug(self):
        url = reverse("service-detail", kwargs={"slug": "trafik"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["title"], "Trafik")
        self.assertIn("body", r.data)
