from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todo_item = get_object_or_404(TodoList, id=id)
    context = {
        "todo_item": todo_item,
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

def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todo_list)
    context = {
        "form": form
    }

    return render(request, "todos/update.html", context)


def todo_list_delete(request, id):
  todo_list = get_object_or_404(TodoList, id=id)
  if request.method == "POST":
    todo_list.delete()
    return redirect("todo_list_list")

  return render(request, "todos/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form
    }
    return render(request, "todos/create-item.html", context)


def todo_item_update(request, id):
    todo_item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoItemForm(instance=todo_item)
    context = {
        "form": form
    }

    return render(request, "todos/update-item.html", context)
