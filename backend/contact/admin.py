from django.contrib import admin

from .models import ContactCard, ContactMessage, ContactSiteProfile


@admin.register(ContactSiteProfile)
class ContactSiteProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactSiteProfile.objects.exists()


@admin.register(ContactCard)
class ContactCardAdmin(admin.ModelAdmin):
    list_display = ("title_label", "kind", "sort_order")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_read")
    list_filter = ("is_read",)
