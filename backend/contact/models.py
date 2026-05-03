from django.db import models


class ContactSiteProfile(models.Model):
    """İletişim sayfası: harita, üst metin (tek kayıt — pk=1)."""

    intro_kicker = models.CharField(max_length=120, blank=True)
    intro_headline = models.CharField(max_length=400, blank=True)
    intro_body = models.TextField(blank=True)
    map_embed_url = models.URLField(max_length=800, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "Contact site profile"

    class Meta:
        verbose_name = "Contact site profile"
        verbose_name_plural = "Contact site profile"


class ContactCard(models.Model):
    class Kind(models.TextChoices):
        ADDRESS = "address", "Address"
        EMAIL = "email", "E-mail"
        PHONE = "phone", "Phone"

    kind = models.CharField(max_length=16, choices=Kind.choices)
    title_label = models.CharField(max_length=80)
    line_primary = models.CharField(max_length=200, blank=True)
    line_secondary = models.CharField(max_length=200, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("sort_order", "id")


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=64, blank=True)
    source_page = models.CharField(max_length=80, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)
