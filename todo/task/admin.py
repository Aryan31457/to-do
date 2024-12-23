from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_status', 'task_created', 'task_completed')
    list_filter = ('task_status', 'task_created')
    search_fields = ('task_name', 'task_description')
