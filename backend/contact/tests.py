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
        payload = {"name": "Ali", "email": "ali@test.com", "message": "Merhaba"}
        r = self.client.post(url, payload, format="json")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.get()
        self.assertEqual(msg.name, "Ali")
