from django.shortcuts import render
from .models import Todo
from django.views import generic
from django import forms
from .forms import todoForm



# Create your views here.
class TodotList(generic.ListView):
    model = Todo
    


class TodoDetail(generic.DetailView):
    model = Todo





def todo_list(request):
    data = Todo.objects.all()
    return render(request, 'todo/todo.html', {'form':data})



def todo_detail(request,todo_id):
    data = Todo.objects.get(id=todo_id)
    return render(request,'todo/detail.html',{'form':data})


def new_post(request):
    form = todoForm()
    return render(request,'todo/new.html',{'form':form})