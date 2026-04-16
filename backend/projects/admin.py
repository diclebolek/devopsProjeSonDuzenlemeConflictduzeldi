from django.contrib import admin

from .models import Project, ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "is_published", "completed_on")
    list_filter = ("is_published", "category")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug")
