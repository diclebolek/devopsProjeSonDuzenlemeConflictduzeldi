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

    @property
    def budget_display(self) -> str:
        if not hasattr(self, "meta") or self.meta.budget_amount is None:
            return ""
        return f"{self.meta.budget_amount} {self.meta.budget_currency}"


class ProjectMeta(models.Model):
    project = models.OneToOneField(Project, related_name="meta", on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    budget_currency = models.CharField(max_length=8, default="USD")
    client_company = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=160, blank=True)
    status_label = models.CharField(max_length=80, blank=True)

    def __str__(self) -> str:
        return f"Meta: {self.project.title}"
