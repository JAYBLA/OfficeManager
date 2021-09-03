from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'invoice'

urlpatterns = [
    path('',home,name = 'app-home'),
    
    #CUSTOMER
    path('customer', customer_create, name='customer-create') ,
    path('customer/<int:customer_id>/', customer_detail, name='customer-detail'),
    path('customers', customer_list, name='customer-list'),
    path('customer/<int:customer_id>/update/', update_customer, name='update-customer'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete_customer'),
    
    #INVOICE
    path('invoice/new/', invoice_create, name='new-invoice'),    
    path('invoice/<int:id>/', invoice_detail, name='invoice-detail'),
    path('Unpaid-invoices', invoice_unpaid, name='invoice-unpaid'),
    path('Paid-invoices', invoice_paid, name='invoice-paid'),
    path('invoices', invoice_list, name='invoice-list'),
    path('Draft-invoices', invoice_draft, name='invoice-draft'),
    
    #ITEMS
    path('invoice/<int:id>/item/add/', OrderItemCreateView.as_view(), name='create_item'),
    path('invoice/<int:id>/<int:pk>/update/', OrderItemUpdateView.as_view(), name='update_item'),
    path('invoice/<int:id>/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='delete_item'),
    path('invoice/<int:invoice_id>/update/', update_invoice, name='update-invoice'),
    path('invoice/<int:pk>/delete/', InvoiceDeleteView.as_view(), name='delete_invoice'),
    path('invoice/<int:invoice_id>/print/', printable_invoice, name='print-invoice'),
    path('invoice/<int:invoice_id>/download/', GeneratePdf.as_view(), name='download-invoice'), 
]