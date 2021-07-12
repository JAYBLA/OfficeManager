from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'invoice'

urlpatterns = [
    path('',home,name = 'app-home'),
    
    #CUSTOMER
    path('customer', customer_create, name='customer-create-list') ,
    path('customer/<int:customer_id>/', customer_detail, name='customer-detail'),
    path('customer/<int:customer_id>/update/', update_customer, name='update-customer'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete_customer'),
    
    #INVOICE
    path('invoice/new/', invoice_create, name='new-invoice'),    
    path('invoice/<int:id>/', invoice_detail, name='invoice-detail'),
    path('invoice/<int:id>/item/add/', add_order_item, name='add-item'),
    path('invoice/<int:invoice_id>/item/<int:invoiceitem_id>/delete/', delete_item, name='delete-item'),
    path('invoice/<int:invoice_id>/update/', update_invoice, name='update-invoice'),
    path('invoice/<int:pk>/delete/', InvoiceDeleteView.as_view(), name='delete_invoice'),
    path('invoice/<int:invoice_id>/print/', printable_invoice, name='print-invoice'),
    path('invoice/<int:invoice_id>/download/', GeneratePdf.as_view(), name='download-invoice'),  
]