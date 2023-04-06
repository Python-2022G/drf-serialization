from django.db import models


class Task(models.Model):
    title       = models.CharField(max_length=64)
    description = models.TextField()
    completed   = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return self.title
    