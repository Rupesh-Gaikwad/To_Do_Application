from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Tasks(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_to_perform")
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_starts_at = models.TimeField()
    task_ends_at = models.TimeField()
    #task_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Tasks'