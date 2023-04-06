# drf-serialization

This is a simple example of how to use Django Rest Framework to serialize data.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Object Task

```python
class Task:
    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed

task = Task('Buy milk', 'Buy 2L of milk from the store', False)
```

Serializer

```python
class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    completed = serializers.BooleanField()
```

Serialize

```python
serializer = TaskSerializer(task)
serializer.data
```

Output

```json
{
    "title": "Buy milk",
    "description": "Buy 2L of milk from the store",
    "completed": false
}
```

Model Task

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
```

Serializer

```python
from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    completed = serializers.BooleanField()
```

Serialize

```python
serializer = TaskSerializer(task)
serializer.data
```

Output

```json
{
    "title": "Buy milk",
    "description": "Buy 2L of milk from the store",
    "completed": false
}
```
