from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Project, ProjectCategory


class ProjectAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        category = ProjectCategory.objects.create(name="Kurumsal", slug="kurumsal")
        Project.objects.create(
            category=category,
            title="Yayinlanan Proje",
            slug="yayinlanan-proje",
            is_published=True,
        )
        Project.objects.create(
            category=category,
            title="Gizli Proje",
            slug="gizli-proje",
            is_published=False,
        )

    def test_project_list_returns_only_published(self):
        r = self.client.get(reverse("project-list"))
        self.assertEqual(r.status_code, 200)
        slugs = [item["slug"] for item in r.data]
        self.assertIn("yayinlanan-proje", slugs)
        self.assertNotIn("gizli-proje", slugs)

    def test_project_detail_404_for_unpublished(self):
        r = self.client.get(reverse("project-detail", kwargs={"slug": "gizli-proje"}))
        self.assertEqual(r.status_code, 404)
