from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

# import models
from .models import Task

# import seralizers
from .serializers import TaskSerializer


@api_view(['GET'])
def get_tasks(request: Request) -> Response:
    '''get all tasks'''
    # all tasks
    tasks = Task.objects.all()
    # task_list
    tasks_list = []
    for task in tasks:
        serializer = TaskSerializer(task)
        tasks_list.append(serializer.data)
    
    return Response(tasks_list)