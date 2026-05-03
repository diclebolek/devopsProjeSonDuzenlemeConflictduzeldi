from rest_framework import serializers

from .models import Project, ProjectCategory, ProjectMeta


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ("id", "name", "slug", "sort_order")


class ProjectListSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "slug",
            "summary",
            "cover_image_path",
            "cover_image_url",
            "client_name",
            "completed_on",
            "category",
            "sort_order",
            "updated_at",
        )

    def get_cover_image_url(self, obj):
        if not obj.cover_image_path:
            return ""
        normalized_path = obj.cover_image_path[1:] if obj.cover_image_path.startswith("./") else obj.cover_image_path
        request = self.context.get("request")
        if request is None:
            return normalized_path
        return request.build_absolute_uri(normalized_path)


class ProjectDetailSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)
    meta = serializers.SerializerMethodField()
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "slug",
            "summary",
            "body",
            "cover_image_path",
            "cover_image_url",
            "client_name",
            "completed_on",
            "category",
            "meta",
            "sort_order",
            "updated_at",
        )

    def get_meta(self, obj):
        if not hasattr(obj, "meta"):
            return None
        return {
            "budget_amount": obj.meta.budget_amount,
            "budget_currency": obj.meta.budget_currency,
            "client_company": obj.meta.client_company,
            "location": obj.meta.location,
            "status_label": obj.meta.status_label,
        }

    def get_cover_image_url(self, obj):
        if not obj.cover_image_path:
            return ""
        normalized_path = obj.cover_image_path[1:] if obj.cover_image_path.startswith("./") else obj.cover_image_path
        request = self.context.get("request")
        if request is None:
            return normalized_path
        return request.build_absolute_uri(normalized_path)


class ProjectMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMeta
        fields = ("budget_amount", "budget_currency", "client_company", "location", "status_label")
