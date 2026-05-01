from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import ContactCard, ContactMessage, ContactSiteProfile


class ContactAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        ContactSiteProfile.objects.create(
            pk=1,
            intro_kicker="Merhaba",
            intro_headline="Bize yazın",
            intro_body="Metin",
        )
        ContactCard.objects.create(
            kind=ContactCard.Kind.EMAIL,
            title_label="E-posta",
            line_primary="a@b.com",
            sort_order=1,
        )

    def test_contact_page_payload(self):
        url = reverse("contact-page")
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["profile"]["intro_kicker"], "Merhaba")
        self.assertEqual(len(r.data["cards"]), 1)

    def test_contact_message_create(self):
        url = reverse("contact-message-create")
        payload = {
            "name": "Ali",
            "email": "ali@test.com",
            "phone": "555",
            "source_page": "contact",
            "message": "Merhaba",
        }
        r = self.client.post(url, payload, format="json")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.get()
        self.assertEqual(msg.name, "Ali")
        self.assertEqual(msg.phone, "555")
        self.assertEqual(msg.source_page, "contact")

    def test_contact_message_invalid_payload(self):
        url = reverse("contact-message-create")
        payload = {"name": "", "email": "wrong-mail", "phone": "555", "source_page": "contact", "message": ""}
        r = self.client.post(url, payload, format="json")
        self.assertEqual(r.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_contact_page_creates_default_profile_when_missing(self):
        ContactSiteProfile.objects.all().delete()
        url = reverse("contact-page")
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(ContactSiteProfile.objects.count(), 1)


class ContactModelTests(TestCase):
    def test_contact_profile_forces_singleton_pk(self):
        profile = ContactSiteProfile(intro_headline="Test")
        profile.save()
        self.assertEqual(profile.pk, 1)

    def test_contact_message_ordering_latest_first(self):
        ContactMessage.objects.create(name="A", email="a@test.com", message="1")
        ContactMessage.objects.create(name="B", email="b@test.com", message="2")
        ordered = list(ContactMessage.objects.values_list("name", flat=True))
        self.assertEqual(ordered[0], "B")
