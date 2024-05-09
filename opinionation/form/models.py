# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 4

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name