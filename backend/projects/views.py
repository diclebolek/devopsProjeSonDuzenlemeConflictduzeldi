from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Project
from .serializers import ProjectDetailSerializer, ProjectListSerializer


class ProjectListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectListSerializer

    def get_queryset(self):
        return Project.objects.filter(is_published=True).select_related("category")


class ProjectDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Project.objects.filter(is_published=True).select_related("category", "meta")
