from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Project, ProjectCategory, ProjectMeta


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
        published = Project.objects.get(slug="yayinlanan-proje")
        ProjectMeta.objects.create(
            project=published,
            budget_amount="45000.00",
            budget_currency="USD",
            status_label="Completed",
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

    def test_project_detail_includes_meta(self):
        r = self.client.get(reverse("project-detail", kwargs={"slug": "yayinlanan-proje"}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("meta", r.data)
        self.assertEqual(r.data["meta"]["budget_currency"], "USD")
        self.assertIn("cover_image_url", r.data)


class ProjectModelTests(TestCase):
    def test_budget_display_property(self):
        category = ProjectCategory.objects.create(name="Kurumsal2", slug="kurumsal2")
        project = Project.objects.create(category=category, title="P1", slug="p1")
        self.assertEqual(project.budget_display, "")
        ProjectMeta.objects.create(project=project, budget_amount="123.45", budget_currency="TRY")
        project.refresh_from_db()
        self.assertEqual(project.budget_display, "123.45 TRY")
