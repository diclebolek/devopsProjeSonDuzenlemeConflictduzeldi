from rest_framework import serializers

from .models import BlogCategory, BlogPost


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ("id", "name", "slug", "sort_order")


class BlogPostListSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "slug",
            "excerpt",
            "cover_image_path",
            "author_display_name",
            "published_at",
            "category",
            "updated_at",
        )


class BlogPostDetailSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "slug",
            "excerpt",
            "body",
            "cover_image_path",
            "author_display_name",
            "published_at",
            "category",
            "updated_at",
        )
