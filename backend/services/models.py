from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("sort_order", "name")
        verbose_name_plural = "Service categories"

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory, related_name="services", on_delete=models.PROTECT
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=160, unique=True, db_index=True)
    short_description = models.CharField(max_length=400, blank=True)
    body = models.TextField(blank=True)
    icon_path = models.CharField(max_length=500, blank=True)
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("sort_order", "title")

    def __str__(self) -> str:
        return self.title

    @property
    def feature_count(self) -> int:
        return self.features.count()


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name="features", on_delete=models.CASCADE)
    text = models.CharField(max_length=220)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("sort_order", "id")

    def __str__(self) -> str:
        return f"{self.service.title}: {self.text}"
