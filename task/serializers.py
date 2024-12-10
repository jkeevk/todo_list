from .models import Task, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'deadline', 'tags', 'is_done', 'created_at']
        read_only_fields = ['created_at', 'is_done']