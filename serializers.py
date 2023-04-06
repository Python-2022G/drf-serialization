from rest_framework import serializers


class Task:
    def __init__(self, title, description, completed=None):
        self.title = title
        self.description = description
        self.completed = completed


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    completed = serializers.BooleanField()


task = Task('Buy milk', 'Buy 2L of milk from the store')

serializer = TaskSerializer(task)
print(
    serializer.data
)