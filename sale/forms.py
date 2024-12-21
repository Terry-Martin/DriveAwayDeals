from django import forms
from .models import Customer, Staff

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'second_name', 'email', 'updated_by']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id', 'first_name', 'second_name', 'email', 'position']

