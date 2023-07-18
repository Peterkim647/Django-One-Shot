from django.db import models
from django.conf import settings


class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
