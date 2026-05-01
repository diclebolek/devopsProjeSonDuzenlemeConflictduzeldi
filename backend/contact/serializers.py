from rest_framework import serializers

from .models import ContactCard, ContactMessage, ContactSiteProfile


class ContactSiteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSiteProfile
        fields = (
            "intro_kicker",
            "intro_headline",
            "intro_body",
            "map_embed_url",
            "updated_at",
        )


class ContactCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactCard
        fields = (
            "kind",
            "title_label",
            "line_primary",
            "line_secondary",
            "sort_order",
        )


class ContactPageSerializer(serializers.Serializer):
    profile = ContactSiteProfileSerializer()
    cards = ContactCardSerializer(many=True)


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ("id", "name", "email", "phone", "source_page", "message", "created_at")
        read_only_fields = ("id", "created_at")
