from django.contrib import admin
from task.models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "description",
        "deadline",
        "display_tags",
        "is_done",
        "created_at",
    ]

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    list_filter = ["tags", "is_done", "created_at"]
    search_fields = ["title", "description"]
    ordering = ["-created_at"]
    list_per_page = 10
    fields = ["title", "description", "deadline", "tags", "is_done", "created_at"]
    readonly_fields = ["created_at"]
    display_tags.short_description = "Теги"
