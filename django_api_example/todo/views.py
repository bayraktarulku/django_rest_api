from django.shortcuts import render
from .models import Todo


def todolist(request):
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render(request, 'todo/simpleTodo.html',
                  {'todolist': todolist,
                   'finishtodos': finishtodos})
