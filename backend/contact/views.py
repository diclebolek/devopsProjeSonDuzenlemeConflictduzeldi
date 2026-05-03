from types import SimpleNamespace

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ContactCard, ContactSiteProfile
from .serializers import ContactMessageSerializer, ContactPageSerializer


class ContactPageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        profile, _ = ContactSiteProfile.objects.get_or_create(pk=1)
        cards = ContactCard.objects.all()
        payload = SimpleNamespace(profile=profile, cards=list(cards))
        return Response(ContactPageSerializer(payload).data)


class ContactMessageCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
