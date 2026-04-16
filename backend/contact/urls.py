from django.urls import path

from .views import ContactMessageCreateView, ContactPageView

urlpatterns = [
    path("", ContactPageView.as_view(), name="contact-page"),
    path("messages/", ContactMessageCreateView.as_view(), name="contact-message-create"),
]
