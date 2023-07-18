from django.shortcuts import render
from todos.models import TodoList


def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list_object": todo_list,
    }
    return render(request, "todos/list.html", context)
