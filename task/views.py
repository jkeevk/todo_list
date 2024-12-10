from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from task.serializers import TaskSerializer, TagSerializer
from task.models import Task, Tag


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = [
        "is_done",
        "tags",
    ]
    search_fields = [
        "title",
    ]
    ordering_fields = ["deadline", "created_at", "title"]
    ordering = ["-created_at"]
    pagination_class = LimitOffsetPagination


class TagsViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = [
        "name",
    ]
    search_fields = [
        "name",
    ]
    pagination_class = LimitOffsetPagination
