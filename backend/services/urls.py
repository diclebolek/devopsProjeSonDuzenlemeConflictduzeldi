from django.urls import path

from .views import ServiceDetailView, ServiceListView

urlpatterns = [
    path("", ServiceListView.as_view(), name="service-list"),
    path("<slug:slug>/", ServiceDetailView.as_view(), name="service-detail"),
]
