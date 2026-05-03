from rest_framework import serializers

from .models import Service, ServiceCategory, ServiceFeature


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ("id", "name", "slug", "description", "sort_order")


class ServiceListSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "icon_path",
            "icon_url",
            "category",
            "sort_order",
            "updated_at",
        )

    def get_icon_url(self, obj):
        if not obj.icon_path:
            return ""
        normalized_path = obj.icon_path[1:] if obj.icon_path.startswith("./") else obj.icon_path
        request = self.context.get("request")
        if request is None:
            return normalized_path
        return request.build_absolute_uri(normalized_path)


class ServiceDetailSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    features = serializers.SerializerMethodField()
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "body",
            "icon_path",
            "icon_url",
            "category",
            "features",
            "sort_order",
            "updated_at",
        )

    def get_features(self, obj):
        return [f.text for f in obj.features.all()]

    def get_icon_url(self, obj):
        if not obj.icon_path:
            return ""
        normalized_path = obj.icon_path[1:] if obj.icon_path.startswith("./") else obj.icon_path
        request = self.context.get("request")
        if request is None:
            return normalized_path
        return request.build_absolute_uri(normalized_path)


class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = ("id", "text", "sort_order")
