from django.contrib import admin
from to_do_App.models import Tasks
# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display=['username','title', 'description', 'task_starts_at', 'task_ends_at', 'created_at', 'updated_at']

admin.site.register(Tasks, TasksAdmin)
