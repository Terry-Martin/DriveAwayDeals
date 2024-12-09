from django.shortcuts import render
from django.views import generic
from .models import Staff, Transaction, CustomerDetail

# Create your views here.
class PostList(generic.ListView):
   queryset = CustomerDetail.objects.all()
   template_name = "post_list.html"
