from django import forms
from .models import Item, Customer

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'second_name', 'email', 'updated_by']
