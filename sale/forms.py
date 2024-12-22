from django import forms
from .models import Customer, Staff, Transaction


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'second_name', 'email', 'updated_by']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'second_name', 'email', 'position']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['car_registration', 'price', 'customer_ID']
