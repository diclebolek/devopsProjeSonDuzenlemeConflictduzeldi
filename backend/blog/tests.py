from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from .models import BlogCategory, BlogComment, BlogPost


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
        published = BlogPost.objects.get(slug="yayinlanan")
        BlogComment.objects.create(
            post=published,
            name="Ali",
            email="ali@test.com",
            message="Yorum",
            is_approved=True,
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

    def test_blog_detail_includes_comments(self):
        r = self.client.get(reverse("blog-detail", kwargs={"slug": "yayinlanan"}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("comments", r.data)
        self.assertEqual(len(r.data["comments"]), 1)
        self.assertIn("cover_image_url", r.data)


class BlogModelTests(TestCase):
    def test_approved_comment_count_property(self):
        category = BlogCategory.objects.create(name="Genel2", slug="genel2")
        post = BlogPost.objects.create(
            category=category,
            title="Model Post",
            slug="model-post",
            body="x",
            is_published=True,
            published_at=timezone.now(),
        )
        BlogComment.objects.create(post=post, name="A", email="a@a.com", message="1", is_approved=True)
        BlogComment.objects.create(post=post, name="B", email="b@a.com", message="2", is_approved=False)
        self.assertEqual(post.approved_comment_count, 1)
