from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("sort_order", "name")
        verbose_name_plural = "Project categories"

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    category = models.ForeignKey(
        ProjectCategory, related_name="projects", on_delete=models.PROTECT
    )
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    summary = models.CharField(max_length=500, blank=True)
    body = models.TextField(blank=True)
    cover_image_path = models.CharField(max_length=500, blank=True)
    client_name = models.CharField(max_length=200, blank=True)
    completed_on = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("sort_order", "title")

    def __str__(self) -> str:
        return self.title
