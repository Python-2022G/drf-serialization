from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=64)
    description = serializers.CharField()
    completed   = serializers.BooleanField(default=False)


    def create(self, validated_data):
        return Task.objects.create(**validated_data)