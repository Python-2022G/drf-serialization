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
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)