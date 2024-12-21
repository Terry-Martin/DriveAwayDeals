from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Staff, Transaction, Customer, Item
from .forms import ItemForm, CustomerForm

# Create your views here.
def homepage(request):
    #return render(request, 'sale/homepage.html')
    # customers = Customer.objects.all()
    return render(request, 'sale/index.html')


def customer_list(request):
   customers = Customer.objects.all()
   return render(request, 'sale/customer_list.html', {'customers': customers})

def staff_list(request):
   staffs = Staff.objects.all()
   return render(request, 'sale/staff_list.html', {'staffs': staffs})

def transaction_list(request):
   transactions = Transaction.objects.all()
   return render(request, 'sale/transaction_list.html', {'transactions': transactions})



def customer_detail(request, customer_id):

   queryset = Customer.objects.all()
   customer = get_object_or_404(queryset, customer_id=customer_id)

   return render(
      request,
      "sale/customer_detail.html",
      {"customer": customer},
   )

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
    customer = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerFormForm(instance=item)
    return render(request, 'sale/customer_form.html', {'form': form, 'action': 'Edit'})



def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'sale/customer_confirm_delete.html', {'customer': customer})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item-list')
    return render(request, 'sale/item_confirm_delete.html', {'item': item})





def item_list(request):
    items = Item.objects.all()
    return render(request, 'sale/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item-list')
    else:
        form = ItemForm()
    return render(request, 'sale/item_form.html', {'form': form, 'action': 'Create'})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item-list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'sale/item_form.html', {'form': form, 'action': 'Edit'})


