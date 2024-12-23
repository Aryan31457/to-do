from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_Task, name='task_create'),
    path('list/', views.task_list, name='task_list'),
    path('edit/<int:task_id>/', views.edit_Task, name='task_edit'),
    path('delete/<int:task_id>/', views.delete_Task, name='task_delete'),
]
