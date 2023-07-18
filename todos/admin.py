from django.contrib import admin
from todos.models import TodoList


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "id",
    ]
