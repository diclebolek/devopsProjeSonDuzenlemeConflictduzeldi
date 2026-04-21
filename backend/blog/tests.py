from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from .models import BlogCategory, BlogPost


class BlogAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        category = BlogCategory.objects.create(name="Genel", slug="genel")
        BlogPost.objects.create(
            category=category,
            title="Yayinlanan",
            slug="yayinlanan",
            body="Body",
            is_published=True,
            published_at=timezone.now(),
        )
        BlogPost.objects.create(
            category=category,
            title="Taslak",
            slug="taslak",
            body="Body",
            is_published=False,
            published_at=timezone.now(),
        )

    def test_blog_list_returns_only_published(self):
        r = self.client.get(reverse("blog-list"))
        self.assertEqual(r.status_code, 200)
        slugs = [item["slug"] for item in r.data]
        self.assertIn("yayinlanan", slugs)
        self.assertNotIn("taslak", slugs)

    def test_blog_detail_404_for_unpublished(self):
        r = self.client.get(reverse("blog-detail", kwargs={"slug": "taslak"}))
        self.assertEqual(r.status_code, 404)
