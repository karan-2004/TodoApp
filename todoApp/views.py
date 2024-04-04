from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models

# Create your views here.
def todo(request):
    if request.method == 'POST':
        op = request.POST['op']
        if op == 'add':
            todo = request.POST['todo']
            todoObj = models.Todo.objects.create(todo=todo)
            todoObj.save()
            return redirect('index')
        elif op == 'delete':
            id = request.POST['id']
            models.Todo.objects.get(id=id).delete()
            return redirect('index')
        elif op == 'update':
            id = request.POST['id']
            obj = models.Todo.objects.get(id=id)
            obj.status = True
            obj.save()
            return redirect('index')



    todoList = models.Todo.objects.all()  
    return render(request, 'index.html', {'todoList':todoList})