from django.db import models

# Create your models here.
class Todos(models.Model):
    todo_id = models.IntegerField()
    todo_task = models.CharField(max_length=100)

    def __str__(self):
        return str(self.todo_id)