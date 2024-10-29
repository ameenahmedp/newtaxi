from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rider(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, unique=True)
    total_no_of_travelers = models.IntegerField(default=1)
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)