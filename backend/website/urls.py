from django.urls import path

from .views import ContentCoverageMapView, SiteSettingView, StaticPageDetailView

urlpatterns = [
    path("coverage-map/", ContentCoverageMapView.as_view(), name="content-coverage-map"),
    path("site-settings/", SiteSettingView.as_view(), name="site-settings"),
    path("<slug:slug>/", StaticPageDetailView.as_view(), name="static-page-detail"),
]
