from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm


def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list_object": todo_list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todo_item_instance = get_object_or_404(TodoList, id=id)
    context = {
        "todo_item_instance": todo_item_instance,
    }
    return render(request, "todos/detail.html", context)

def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list_list")
    else:
        form = TodoListForm()
    context = {
        "form": form
    }
    return render(request, "todos/create.html", context)
