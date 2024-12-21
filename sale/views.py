from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Staff, Transaction, Customer
from .forms import CustomerForm, StaffForm, TransactionForm

# Create your views here.
def homepage(request):
    return render(request, 'sale/index.html')


def customer_list(request):
   customers = Customer.objects.all()
   return render(request, 'sale/customer_list.html', {'customers': customers})


def customer_detail(request, pk):
   queryset = Customer.objects.all()
   customer = get_object_or_404(queryset, pk=pk)

   return render(
      request,
      "sale/customer_detail.html",
      {"customer": customer},)


def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'sale/customer_form.html', {'form': form, 'action': 'Create'})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'sale/customer_form.html', {'form': form, 'action': 'Edit'})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'sale/customer_confirm_delete.html', {'customer': customer})


def staff_list(request):
   staffs = Staff.objects.all()
   return render(request, 'sale/staff_list.html', {'staffs': staffs})


def staff_detail(request, pk):
   queryset = Staff.objects.all()
   staff = get_object_or_404(queryset, pk=pk)

   return render(
      request,
      "sale/staff_detail.html",
      {"staff": staff},)


def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'sale/staff_form.html', {'form': form, 'action': 'Create'})


def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'sale/staff_form.html', {'form': form, 'action': 'Edit'})


def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'sale/staff_confirm_delete.html', {'staff': staff})


def transaction_list(request):
   transactions = Transaction.objects.all()
   return render(request, 'sale/transaction_list.html', {'transactions': transactions})


def transaction_detail(request, pk):
   queryset = Transaction.objects.all()
   transaction = get_object_or_404(queryset, pk=pk)

   return render(
      request,
      "sale/transaction_detail.html",
      {"transaction": transaction},)


def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'sale/transaction_form.html', {'form': form, 'action': 'Create'})


def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'sale/transaction_form.html', {'form': form, 'action': 'Edit'})


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'sale/transaction_confirm_delete.html', {'transaction': transaction})




