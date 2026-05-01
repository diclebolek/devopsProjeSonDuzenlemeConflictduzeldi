from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Service
from .serializers import ServiceDetailSerializer, ServiceListSerializer


class ServiceListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceListSerializer

    def get_queryset(self):
        return Service.objects.filter(is_published=True).select_related("category")


class ServiceDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ServiceDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Service.objects.filter(is_published=True).select_related("category").prefetch_related("features")
