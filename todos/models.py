from django.db import models
from django.conf import settings


class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)


class TodoItem(models.Model):
    task = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True, blank=True,)
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(
        TodoList,
        related_name="items",
        on_delete=models.CASCADE,
        null=True,
    )
