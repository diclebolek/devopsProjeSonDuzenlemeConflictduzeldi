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

    def test_retrieve_home(self):
        url = reverse("static-page-detail", kwargs={"slug": "home"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["slug"], "home")
