from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'customer'

urlpatterns = [  
    #CUSTOMER
    path('customer', CustomerCreateView.as_view(), name='customer-create') ,
    path('customer/<int:customer_id>/', customer_detail, name='customer-detail'),
    path('customers', customer_list, name='customer-list'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='update-customer'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete_customer'),
]