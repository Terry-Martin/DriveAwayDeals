from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # Root URL for the homepage

    path('staffs/', views.staff_list, name='staff_list'),
    path('staffs/create/', views.staff_create, name='staff-create'),
    path('staffs/<int:pk>/edit/', views.staff_edit, name='staff-edit'),
    path('staffs/<int:pk>/delete/', views.staff_delete, name='staff-delete'),
    path('staffs/<int:pk>/', views.staff_detail, name='staff_detail'),


    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer-create'),
    path('customers/<int:pk>/edit/', views.customer_edit, name='customer-edit'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer-delete'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),


    path('transactions/', views.transaction_list, name='transaction_list'),




]