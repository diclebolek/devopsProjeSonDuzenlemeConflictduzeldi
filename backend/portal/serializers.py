from rest_framework import serializers

from .models import ClaimTicket, CustomerAlert, InsurancePolicy, InsuranceQuote, PaymentNotice


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = (
            "id",
            "policy_number",
            "product_name",
            "insurer_name",
            "premium_amount",
            "currency",
            "start_date",
            "end_date",
            "status",
            "created_at",
        )


class InsuranceQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceQuote
        fields = (
            "id",
            "reference_code",
            "product_type",
            "offered_premium",
            "status",
            "valid_until",
            "notes",
            "created_at",
        )


class ClaimTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimTicket
        fields = (
            "id",
            "claim_number",
            "incident_date",
            "description",
            "status",
            "created_at",
        )


class PaymentNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentNotice
        fields = (
            "id",
            "due_date",
            "amount",
            "description",
            "status",
            "created_at",
        )


class CustomerAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAlert
        fields = ("id", "title", "body", "is_read", "created_at")
