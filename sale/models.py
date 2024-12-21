from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STAFF_POSITION = (
    ('salesperson','SALESPERSON'),
    ('manager', 'MANAGER'),
)
class Staff(models.Model):
    staff_id = models.PositiveIntegerField(primary_key=True)
    hire_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=60)
    position = models.CharField(max_length=11, choices=STAFF_POSITION, default = "salesperson")

    def __str__(self):
        return self.first_name + " " + self.second_name + "(" + str(self.staff_id) + ") - " + self.position

class Customer(models.Model):
    customer_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        Staff, on_delete = models.SET_NULL, null=True, related_name="updated_by_who"

    )

    def __str__(self):
        return self.first_name + " " + self.second_name + "(" + str(self.customer_id) + ")"

    
TYPE_OF_TRANSACTION = (
    ('sale','SALE'),
    ('purchase', 'PURCHASE'),
)
class Transaction(models.Model):
    transaction_number = models.PositiveIntegerField(primary_key=True)
    transaction_type = models.CharField(max_length=8, choices=TYPE_OF_TRANSACTION, default='sale')
    car_registration = models.CharField(max_length=14)
    price = models.DecimalField(max_digits= 9, decimal_places=2)
    date_completed = models.DateTimeField
    customer_ID = models.ForeignKey(
        Customer, on_delete = models.SET_NULL, null=True, related_name="customer_id_transaction"
    )

    def __str__(self):
        return str(self.transaction_number) + " " + self.transaction_type 

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



    
