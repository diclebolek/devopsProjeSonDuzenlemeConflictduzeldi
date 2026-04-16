from django.conf import settings
from django.db import models


class InsurancePolicy(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Aktif"
        LAPSED = "lapsed", "Süresi doldu"
        CANCELLED = "cancelled", "İptal"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="policies",
    )
    policy_number = models.CharField(max_length=64, unique=True)
    product_name = models.CharField(max_length=200)
    insurer_name = models.CharField(max_length=200, blank=True)
    premium_amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=8, default="TRY")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-end_date",)


class InsuranceQuote(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Taslak"
        SENT = "sent", "Gönderildi"
        ACCEPTED = "accepted", "Kabul"
        REJECTED = "rejected", "Red"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quotes",
    )
    reference_code = models.CharField(max_length=40, unique=True)
    product_type = models.CharField(max_length=120)
    offered_premium = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.SENT)
    valid_until = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)


class ClaimTicket(models.Model):
    class Status(models.TextChoices):
        OPEN = "open", "Açık"
        REVIEW = "review", "İncelemede"
        CLOSED = "closed", "Kapandı"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="claims",
    )
    claim_number = models.CharField(max_length=40, unique=True)
    incident_date = models.DateField()
    description = models.TextField(blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.OPEN)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)


class PaymentNotice(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Bekliyor"
        PAID = "paid", "Ödendi"
        OVERDUE = "overdue", "Gecikmiş"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="payment_notices",
    )
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=240, blank=True)
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("due_date",)


class CustomerAlert(models.Model):
    """Müşteri paneli: bildirimler (5. korumalı sayfa verisi)."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="alerts",
    )
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
