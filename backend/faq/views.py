from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import FAQEntry
from .serializers import FAQEntrySerializer


class FAQListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FAQEntrySerializer

    def get_queryset(self):
        return FAQEntry.objects.filter(is_active=True)
