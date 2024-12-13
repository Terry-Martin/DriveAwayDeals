from django.shortcuts import render
from django.views import generic
from .models import Staff, Transaction, Customer

# Create your views here.
def homepage(request):
    #return render(request, 'sale/homepage.html')
    # customers = Customer.objects.all()
    return render(request, 'sale/index.html')


def customer_list(request):
   customers = Customer.objects.all()
   return render(request, 'sale/customer_list.html', {'customers': customers})

   #queryset = CustomerDetail.objects.all()
   #template_name = "sale/index.html"
   #paginate_by = 6

def staff_list(request):
   staffs = Staff.objects.all()
   return render(request, 'sale/staff_list.html', {'staffs': staffs})

def transaction_list(request):
   transactions = Transaction.objects.all()
   return render(request, 'sale/transaction_list.html', {'transactions': transactions})


