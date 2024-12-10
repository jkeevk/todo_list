from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from task.serializers import TaskSerializer
from task.models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = [
        "title",
    ]
    search_fields = [
        "title",
        "description",
    ]
    pagination_class = LimitOffsetPagination