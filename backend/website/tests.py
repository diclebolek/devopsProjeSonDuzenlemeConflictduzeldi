from django.db import IntegrityError
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import PageSection, SiteSetting, SocialLink, StaticPage


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
        page = StaticPage.objects.get(slug="home")
        PageSection.objects.create(page=page, key="hero", image_path="./assets/img/home.png", sort_order=1)
        url = reverse("static-page-detail", kwargs={"slug": "home"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["slug"], "home")
        self.assertIn("image_url", r.data["sections"][0])

    def test_retrieve_about(self):
        url = reverse("static-page-detail", kwargs={"slug": "about"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["meta_title"], "About")

    def test_missing_slug_returns_404(self):
        url = reverse("static-page-detail", kwargs={"slug": "missing"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 404)


class WebsiteModelTests(TestCase):
    def test_site_setting_is_singleton_and_property_works(self):
        setting = SiteSetting(site_name="Insucom", support_email="info@example.com", support_phone="555")
        setting.save()
        self.assertEqual(setting.pk, 1)
        self.assertEqual(setting.primary_contact, "info@example.com / 555")

    def test_social_link_str_falls_back_to_platform(self):
        link = SocialLink.objects.create(platform=SocialLink.Platform.TWITTER, url="https://x.com/test")
        self.assertEqual(str(link), "twitter")

    def test_page_section_unique_together(self):
        page = StaticPage.objects.create(slug="faq", meta_title="FAQ")
        PageSection.objects.create(page=page, key="intro", title="Intro")
        with self.assertRaises(IntegrityError):
            PageSection.objects.create(page=page, key="intro", title="Dup")


class SiteSettingAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_site_settings_endpoint_returns_payload(self):
        SiteSetting.objects.create(
            pk=1,
            site_name="Insucom",
            support_email="info@example.com",
            support_phone="(629) 555-0129",
        )
        SocialLink.objects.create(
            platform=SocialLink.Platform.FACEBOOK,
            label="Facebook",
            url="https://facebook.com",
            sort_order=1,
            is_active=True,
        )
        response = self.client.get(reverse("site-settings"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["site_name"], "Insucom")
        self.assertEqual(len(response.data["social_links"]), 1)

    def test_coverage_map_lists_all_11_pages(self):
        call_command("seed_demo_data")
        response = self.client.get(reverse("content-coverage-map"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["pages"]), 11)
        project_details = next(page for page in response.data["pages"] if page["html"] == "project-details.html")
        self.assertIn("contract", project_details)
        self.assertIn("mock_data_check", project_details)
        self.assertTrue(project_details["mock_data_check"]["not_null"])
        self.assertTrue(project_details["mock_data_check"]["html_static_match"]["is_match"])
