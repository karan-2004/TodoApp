from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length = 100)
    status = models.BooleanField(default = 0)

    class Meta:
        ordering = ['status']
