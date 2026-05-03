from django.contrib import admin

from .models import FAQEntry


@admin.register(FAQEntry)
class FAQEntryAdmin(admin.ModelAdmin):
    list_display = ("question", "sort_order", "is_active")
    list_filter = ("is_active",)
