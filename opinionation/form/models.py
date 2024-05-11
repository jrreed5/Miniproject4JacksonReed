# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 4

from django.db import models


class SubmittedFormData(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name