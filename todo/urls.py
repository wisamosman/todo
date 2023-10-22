from django.urls import path
from .views import TodotList, TodoDetail , todo_list, todo_detail,new_post
from .api import TodoListAPI , TodoDetailAPI


app_name='todo'


urlpatterns = [
    #path('api/list' , TodoListAPI.as_view()),
    #path('api/list/<int:pk>' , TodoDetailAPI.as_view()),
    
    path('todo/', todo_list),
    path('todo/<int:todo_id>', todo_detail),
    path('todo/new', new_post),
    
    ]