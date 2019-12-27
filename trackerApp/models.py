from django.db import models

# Create your models here.
class Task(models.Model):
    author = models.CharField(max_length=400)
    task = models.CharField(max_length=400)
    assigned = models.CharField(max_length=200)

    def __str__(self):
        return self.author