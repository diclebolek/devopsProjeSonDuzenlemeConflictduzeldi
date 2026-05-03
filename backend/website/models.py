from django.db import models


class SiteSetting(models.Model):
    """Global header/footer ve iletişim verileri (tek kayıt)."""

    site_name = models.CharField(max_length=120, default="Insucom")
    support_email = models.EmailField(blank=True)
    support_phone = models.CharField(max_length=64, blank=True)
    address_line = models.CharField(max_length=250, blank=True)
    copyright_text = models.CharField(max_length=250, blank=True)
    terms_url = models.URLField(max_length=500, blank=True)
    privacy_url = models.URLField(max_length=500, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.site_name

    @property
    def primary_contact(self) -> str:
        if self.support_email and self.support_phone:
            return f"{self.support_email} / {self.support_phone}"
        return self.support_email or self.support_phone

    class Meta:
        verbose_name = "Site setting"
        verbose_name_plural = "Site setting"


class SocialLink(models.Model):
    class Platform(models.TextChoices):
        FACEBOOK = "facebook", "Facebook"
        INSTAGRAM = "instagram", "Instagram"
        TWITTER = "twitter", "Twitter"
        LINKEDIN = "linkedin", "LinkedIn"
        YOUTUBE = "youtube", "YouTube"
        OTHER = "other", "Other"

    platform = models.CharField(max_length=20, choices=Platform.choices, default=Platform.OTHER)
    label = models.CharField(max_length=80, blank=True)
    url = models.URLField(max_length=500)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("sort_order", "id")

    def __str__(self) -> str:
        return self.label or self.platform


class StaticPage(models.Model):
    """Ana sayfa, ikinci ana sayfa, hakkımızda gibi statik şablonların üst verisi."""

    slug = models.SlugField(max_length=64, unique=True, db_index=True)
    meta_title = models.CharField(max_length=200)
    hero_headline = models.CharField(max_length=400, blank=True)
    hero_subheadline = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("slug",)

    def __str__(self) -> str:
        return self.slug


class PageSection(models.Model):
    """Sayfa içi bloklar (Insucom HTML bölümlerine karşılık)."""

    page = models.ForeignKey(
        StaticPage, related_name="sections", on_delete=models.CASCADE
    )
    key = models.SlugField(max_length=64)
    title = models.CharField(max_length=400, blank=True)
    body = models.TextField(blank=True)
    image_path = models.CharField(
        max_length=500,
        blank=True,
        help_text="Örn. ./assets/img/... — frontend statik dosya yolu",
    )
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("page", "sort_order", "id")
        unique_together = ("page", "key")

    def __str__(self) -> str:
        return f"{self.page.slug}:{self.key}"


class PageStatistic(models.Model):
    """Hakkımızda vb. sayfalardaki sayaç / özet kutuları."""

    page = models.ForeignKey(
        StaticPage, related_name="statistics", on_delete=models.CASCADE
    )
    label = models.CharField(max_length=120)
    value = models.CharField(max_length=80)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("page", "sort_order", "id")
