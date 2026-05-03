from django.contrib import admin

from .models import PageSection, PageStatistic, SiteSetting, SocialLink, StaticPage


class PageSectionInline(admin.TabularInline):
    model = PageSection
    extra = 0


class PageStatisticInline(admin.TabularInline):
    model = PageStatistic
    extra = 0


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ("slug", "meta_title", "updated_at")
    inlines = (PageSectionInline, PageStatisticInline)


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("site_name", "support_email", "support_phone", "updated_at")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "label", "url", "is_active", "sort_order")
    list_filter = ("platform", "is_active")
