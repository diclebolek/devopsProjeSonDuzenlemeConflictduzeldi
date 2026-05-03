from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Service, ServiceCategory, ServiceFeature


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
        trafik = Service.objects.get(slug="trafik")
        ServiceFeature.objects.create(service=trafik, text="Coverage Review", sort_order=1)
        ServiceFeature.objects.create(service=trafik, text="Business Insurance", sort_order=2)
        Service.objects.create(
            category=cat,
            title="Yayin Disi",
            slug="yayin-disi",
            short_description="Kısa",
            body="Uzun",
            is_published=False,
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
        self.assertIn("features", r.data)
        self.assertEqual(len(r.data["features"]), 2)
        self.assertIn("icon_url", r.data)

    def test_list_hides_unpublished(self):
        url = reverse("service-list")
        r = self.client.get(url)
        slugs = [item["slug"] for item in r.data]
        self.assertNotIn("yayin-disi", slugs)

    def test_detail_returns_404_for_unpublished(self):
        url = reverse("service-detail", kwargs={"slug": "yayin-disi"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 404)


class ServiceModelTests(TestCase):
    def test_service_feature_count_property(self):
        cat = ServiceCategory.objects.create(name="Model", slug="model-cat")
        service = Service.objects.create(category=cat, title="Konut", slug="konut")
        ServiceFeature.objects.create(service=service, text="F1")
        ServiceFeature.objects.create(service=service, text="F2")
        self.assertEqual(service.feature_count, 2)

    def test_service_feature_str(self):
        cat = ServiceCategory.objects.create(name="Model2", slug="model-cat-2")
        service = Service.objects.create(category=cat, title="DASK", slug="dask-model")
        feature = ServiceFeature.objects.create(service=service, text="Teminat")
        self.assertEqual(str(feature), "DASK: Teminat")
