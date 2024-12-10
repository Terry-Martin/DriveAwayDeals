from django.contrib import admin
from .models import Customer, Transaction, Staff

# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Staff)