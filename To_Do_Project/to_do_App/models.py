from django.db import models

# Create your models here.
class Tasks(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_starts_at = models.TimeField()
    task_ends_at = models.TimeField()

    class Meta:
        verbose_name_plural = 'Tasks'