from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import StaticPage


class StaticPageAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        StaticPage.objects.create(
            slug="home",
            meta_title="Ana",
            hero_headline="Hoş geldiniz",
        )
        StaticPage.objects.create(
            slug="about",
            meta_title="About",
            hero_headline="Biz Kimiz",
        )

    def test_retrieve_home(self):
        url = reverse("static-page-detail", kwargs={"slug": "home"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["slug"], "home")

    def test_retrieve_about(self):
        url = reverse("static-page-detail", kwargs={"slug": "about"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["meta_title"], "About")

    def test_missing_slug_returns_404(self):
        url = reverse("static-page-detail", kwargs={"slug": "missing"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 404)
