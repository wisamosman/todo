from django.urls import path
from .views import TodotList, TodoDetail
from .api import TodoListAPI , TodoDetailAPI


app_name='todo'


urlpatterns = [
    path('api/list' , TodoListAPI.as_view()),
    path('api/list/<int:pk>' , TodoDetailAPI.as_view()),
    
    ]