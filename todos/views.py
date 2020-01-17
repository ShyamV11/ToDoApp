from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import ToDo

# Create your views here.
def list_todos_items(request):
    context = {'todos_list' : ToDo.objects.all()}
    return render(request,'todos/todo_list.html',context)

def insert_todos_item(request:HttpRequest):
    todo = ToDo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def delete_todos_item(request,todo_id):
    todo_to_delete = ToDo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')
