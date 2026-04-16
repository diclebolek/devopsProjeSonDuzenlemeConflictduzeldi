from django.urls import include, path

urlpatterns = [
    path("pages/", include("website.urls")),
    path("services/", include("services.urls")),
    path("blog/", include("blog.urls")),
    path("projects/", include("projects.urls")),
    path("faq/", include("faq.urls")),
    path("contact/", include("contact.urls")),
    path("auth/", include("accounts.urls")),
    path("me/", include("portal.urls")),
]
