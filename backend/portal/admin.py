from django.contrib import admin

from .models import ClaimTicket, CustomerAlert, InsurancePolicy, InsuranceQuote, PaymentNotice


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ("policy_number", "user", "product_name", "status", "end_date")
    search_fields = ("policy_number", "user__username")


@admin.register(InsuranceQuote)
class InsuranceQuoteAdmin(admin.ModelAdmin):
    list_display = ("reference_code", "user", "product_type", "status")


@admin.register(ClaimTicket)
class ClaimTicketAdmin(admin.ModelAdmin):
    list_display = ("claim_number", "user", "status", "incident_date")


@admin.register(PaymentNotice)
class PaymentNoticeAdmin(admin.ModelAdmin):
    list_display = ("user", "due_date", "amount", "status")


@admin.register(CustomerAlert)
class CustomerAlertAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "is_read", "created_at")
