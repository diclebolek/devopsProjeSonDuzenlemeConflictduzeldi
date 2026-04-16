from rest_framework import serializers

from .models import Project, ProjectCategory


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ("id", "name", "slug", "sort_order")


class ProjectListSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "slug",
            "summary",
            "cover_image_path",
            "client_name",
            "completed_on",
            "category",
            "sort_order",
            "updated_at",
        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "slug",
            "summary",
            "body",
            "cover_image_path",
            "client_name",
            "completed_on",
            "category",
            "sort_order",
            "updated_at",
        )
