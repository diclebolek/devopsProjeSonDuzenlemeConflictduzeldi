from rest_framework import serializers

from .models import PageSection, PageStatistic, StaticPage


class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSection
        fields = ("key", "title", "body", "image_path", "sort_order")


class PageStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageStatistic
        fields = ("label", "value", "sort_order")


class StaticPageSerializer(serializers.ModelSerializer):
    sections = PageSectionSerializer(many=True, read_only=True)
    statistics = PageStatisticSerializer(many=True, read_only=True)

    class Meta:
        model = StaticPage
        fields = (
            "slug",
            "meta_title",
            "hero_headline",
            "hero_subheadline",
            "intro",
            "updated_at",
            "sections",
            "statistics",
        )
