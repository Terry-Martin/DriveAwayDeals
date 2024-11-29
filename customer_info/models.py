from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerDetails(models.Model):
    customerID = models.IntegerField(unique=True)
    slug = models.IntegerField(unique=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    
