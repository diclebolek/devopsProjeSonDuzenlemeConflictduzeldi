from rest_framework import serializers

from .models import Service, ServiceCategory


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ("id", "name", "slug", "description", "sort_order")


class ServiceListSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)

    class Meta:
        model = Service
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "icon_path",
            "category",
            "sort_order",
            "updated_at",
        )


class ServiceDetailSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)

    class Meta:
        model = Service
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "body",
            "icon_path",
            "category",
            "sort_order",
            "updated_at",
        )
