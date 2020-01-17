from django.urls import path
from . import views


urlpatterns = [
    path('list/',views.list_todos_items)
    path('insert_todos/',views.insert_todos_item, name='insert_todos_item')
    path('delete_todos/<int:todo_id>/', views.delete_todos_item, name='delete_todos_item')
