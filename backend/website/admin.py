from django.contrib import admin

from .models import PageSection, PageStatistic, StaticPage


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
