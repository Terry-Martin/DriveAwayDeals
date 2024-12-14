from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # Root URL for the homepage
    path('customers/', views.customer_list, name='customer_list'),
    path('staffs/', views.staff_list, name='staff_list'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('<int:customer_id>/', views.customer_detail, name='customer_detail'),

]