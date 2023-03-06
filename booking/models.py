from django.db import models

# Create your models here.
from django.db import models

class Salon(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Stylist(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='stylists') 
    """
    stylist is many to one (many stylist to one)
    """
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=255)
    appointment_time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.customer_name}  {self.stylist.name}"
