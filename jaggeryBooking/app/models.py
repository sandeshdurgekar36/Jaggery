from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=10 ,blank=True)
    full_name = models.CharField(max_length=30,blank=True, null=True, unique=True)
    address = models.TextField(blank=True, null=True)
    groups = None
    user_permissions = None

    def __str__(self) -> str:
        return self.username
    
class Product(models.Model):
    product_name = models.CharField(max_length=100,blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    qty = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self) -> str:
        return self.product_name

class AvailableSlots(models.Model):
    slots_date_time = models.DateTimeField(blank=True, null=True)
    display = models.BooleanField(default=True)

class UsersBookedSlots(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
    slots = models.ForeignKey(AvailableSlots, on_delete=models.CASCADE, blank=True, null=True)

class UserOrders(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
    product_details = models.JSONField(blank=True, null=True)
    total_amount_to_be_paid = models.CharField(max_length=100,blank=True, null=True) 
    mode_of_payment = models.CharField(max_length=100,blank=True, null=True) 

