from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)