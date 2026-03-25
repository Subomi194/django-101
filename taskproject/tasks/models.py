from django.db import models
from django.contrib.auth.models import User 

#CREATE A DATABASE TABLE NAMED TASKS
class Task(models.Model):
    # Add this line to link each task to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Create your models here.
