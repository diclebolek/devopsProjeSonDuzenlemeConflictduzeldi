from django.db import models


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
