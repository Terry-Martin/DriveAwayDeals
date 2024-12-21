from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # Root URL for the homepage
    path('customers/', views.customer_list, name='customer_list'),
    path('staffs/', views.staff_list, name='staff_list'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('<int:customer_id>/', views.customer_detail, name='customer_detail'),

    #path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer-create'),
    path('<int:pk>/edit/', views.customer_edit, name='customer-edit'),
    path('<int:pk>/delete/', views.customer_delete, name='customer-delete'),

    #path('', views.item_list, name='item-list'),
    #path('create/', views.item_create, name='item-create'),
    #path('<int:pk>/edit/', views.item_edit, name='item-edit'),
    #path('<int:pk>/delete/', views.item_delete, name='item-delete'),


]