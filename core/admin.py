from django.contrib import admin

from .models import Project, Task, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'name',
        'description',
        'owner__username',
    )

    filter_horizontal = (
        'members',
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project',
        'assigned_to',
        'status',
        'priority',
        'due_date',
    )

    list_filter = (
        'status',
        'priority',
    )

    search_fields = (
        'title',
        'description',
        'project__name',
        'assigned_to__username',
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'task',
        'author',
        'created_at',
    )
    search_fields = (
        'content',
        'author__username',
        'task__title',
    )
    list_filter = ('created_at',)