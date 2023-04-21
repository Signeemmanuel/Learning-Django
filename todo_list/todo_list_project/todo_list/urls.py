from django.urls import path
from .views import TodoItemList, TodoItemDetail

urlpatterns = [
    path('todos/', TodoItemList.as_view(), name='todo_list'),
    path('todos/<int:pk>', TodoItemDetail.as_view(), name='todo_details')
]