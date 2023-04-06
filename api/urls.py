from django.urls import path
from .views import get_tasks, create_task, update_task

urlpatterns = [
    path('tasks', get_tasks),
    path('create', create_task),
    path('update/<int:pk>', update_task),
]
