from django.contrib import admin
from .models import CustomerDetail, Transaction, Staff

# Register your models here.
admin.site.register(CustomerDetail)
admin.site.register(Transaction)
admin.site.register(Staff)