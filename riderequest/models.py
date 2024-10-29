from django.db import models
from ..driver.models import Driver
from ..rider.models import Rider
# Create your models here.

class RideRequest(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride Request from {self.rider} to {self.dropoff_location} - Status: {self.status}"
