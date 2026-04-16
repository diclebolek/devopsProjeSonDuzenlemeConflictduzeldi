from django.urls import path

from .views import StaticPageDetailView

urlpatterns = [
    path("<slug:slug>/", StaticPageDetailView.as_view(), name="static-page-detail"),
]
