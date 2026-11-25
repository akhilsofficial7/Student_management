from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentDb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name