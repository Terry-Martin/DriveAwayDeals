from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    hire_date = models.DateTimeField(auto_now_add=True)
    first_name = models.TextField
    second_name = models.TextField
    email = models.EmailField
    position = models.TextField

class Transaction(models.Model):
    transaction_number = models.IntegerField(primary_key=True)
    #customer_ID = models.ForeignKey(
        #CustomerDetail, on_delete = models.RESTRICT, related_name="customer_id"
    #)
    transaction_type = models.TextField
    car_registration = models.TextField
    price = models.DecimalField(max_digits= 9, decimal_places=2)
    date_completed = models.DateTimeField
    #
    # updated_by =  models.ForeignKey(
        #Staff, on_delete = models.RESTRICT, related_name="staff_id"
    #)
    
class CustomerDetail(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.TextField
    second_name = models.TextField
    email = models.EmailField
    created_on = models.DateTimeField(auto_now_add=True)
    #updated_by = models.ForeignKey(
        #Staff, on_delete = models.RESTRICT, related_name="staff_id"
    #)
   # transaction_number = models.ForeignKey(
      #  Transaction, on_delete = models.RESTRICT, related_name="transaction_number"
    #)


    
