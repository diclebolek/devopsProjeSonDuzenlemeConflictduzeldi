from django.urls import path

from .views import (
    AlertListView,
    ClaimListView,
    PaymentListView,
    PolicyListView,
    QuoteListView,
)

urlpatterns = [
    path("policies/", PolicyListView.as_view(), name="me-policies"),
    path("quotes/", QuoteListView.as_view(), name="me-quotes"),
    path("claims/", ClaimListView.as_view(), name="me-claims"),
    path("payments/", PaymentListView.as_view(), name="me-payments"),
    path("alerts/", AlertListView.as_view(), name="me-alerts"),
]
