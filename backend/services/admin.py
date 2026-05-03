from django.contrib import admin

from .models import Service, ServiceCategory, ServiceFeature


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "is_published", "sort_order")
    list_filter = ("is_published", "category")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug")


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ("service", "text", "sort_order")
    list_filter = ("service",)
