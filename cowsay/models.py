from django.db import models
from django.utils import timezone

# Create your models here.

class UserInput(models.Model):
    user_input = models.TextField()
    date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_input
    

