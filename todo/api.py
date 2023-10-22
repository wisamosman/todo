from .serializers import TodoSerializer
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics



class TodoListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_fields = ['status','name']
    


class TodoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer