from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'customer'

urlpatterns = [  
    #CUSTOMER
    path('create/', CustomerCreateView.as_view(), name='customer-create') ,
    path('<int:customer_id>/', customer_detail, name='customer-detail'),
    path('list/', customer_list, name='customer-list'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='update-customer'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete_customer'),
]