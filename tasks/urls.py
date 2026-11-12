from django.urls import path
from .views import *


urlpatterns = [
    path('categories/',category_list, name='category-list'),
    path('categories/create/', category_create, name='category-create'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('categories/<int:pk>/update/',category_update, name='category-update'),
    path('categories/<int:pk>/delete/',category_delete, name='category-delete'),
    path('tasks/', task_list, name='task-list'),
    path('tasks/create/', task_create, name='task-create'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),
    path('tasks/<int:pk>/update/', task_update, name='task-update'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete'),
]