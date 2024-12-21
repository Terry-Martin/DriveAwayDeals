from django import forms
from .models import Customer, Staff, Transaction

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'second_name', 'email', 'updated_by']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id', 'first_name', 'second_name', 'email', 'position']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_number', 'car_registration', 'price', 'customer_ID']