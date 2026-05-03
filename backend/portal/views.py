from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import ClaimTicket, CustomerAlert, InsurancePolicy, InsuranceQuote, PaymentNotice
from .serializers import (
    ClaimTicketSerializer,
    CustomerAlertSerializer,
    InsurancePolicySerializer,
    InsuranceQuoteSerializer,
    PaymentNoticeSerializer,
)


class PolicyListView(ListAPIView):
    serializer_class = InsurancePolicySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InsurancePolicy.objects.filter(user=self.request.user)


class QuoteListView(ListAPIView):
    serializer_class = InsuranceQuoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InsuranceQuote.objects.filter(user=self.request.user)


class ClaimListView(ListAPIView):
    serializer_class = ClaimTicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ClaimTicket.objects.filter(user=self.request.user)


class PaymentListView(ListAPIView):
    serializer_class = PaymentNoticeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PaymentNotice.objects.filter(user=self.request.user)


class AlertListView(ListAPIView):
    serializer_class = CustomerAlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomerAlert.objects.filter(user=self.request.user)
