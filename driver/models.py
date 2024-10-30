from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carname = models.CharField(max_length=50)
    CAR_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
        ('mpv', 'MPV'),s
    ]

    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, unique=True)
    location = models.PointField()  # current driver location (latitude, longitude)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.carname}"

class Vehicle(models.Model):
    owner = models.OneToOneField(Driver,on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20)  # e.g., 'SUV', 'Sedan'
    vehicle_name = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=15)  # Vehicle registration number
    vehicle_brand = models.CharField(max_length=15)
    capacity = models.PositiveIntegerField(default=4)  # Number of passengers
    color = models.CharField(max_length=30, blank=True)  # Vehicle color
    driver = models.OneToOneField('Driver', on_delete=models.CASCADE)  # Link to the Driver
    def __str__(self):
        return f"{self.vehicle_name} - {self.vehicle_brand}"

