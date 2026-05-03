from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomerProfile

User = get_user_model()
if admin.site.is_registered(User):
    admin.site.unregister(User)


class CustomerProfileInline(admin.StackedInline):
    model = CustomerProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (CustomerProfileInline,)
