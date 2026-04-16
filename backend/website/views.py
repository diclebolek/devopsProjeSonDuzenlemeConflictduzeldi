from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import StaticPage
from .serializers import StaticPageSerializer


class StaticPageDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = StaticPageSerializer
    lookup_field = "slug"
    queryset = StaticPage.objects.prefetch_related("sections", "statistics").all()
