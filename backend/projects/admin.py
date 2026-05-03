from django.contrib import admin

from .models import Project, ProjectCategory, ProjectMeta


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "is_published", "completed_on")
    list_filter = ("is_published", "category")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug")


@admin.register(ProjectMeta)
class ProjectMetaAdmin(admin.ModelAdmin):
    list_display = ("project", "budget_amount", "budget_currency", "status_label")
    search_fields = ("project__title", "client_company")
