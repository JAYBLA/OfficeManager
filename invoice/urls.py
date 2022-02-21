from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'invoice'

urlpatterns = [
    #INVOICE
    path('invoice/new/', invoice_create, name='new-invoice'),    
    path('invoice/<int:id>/', invoice_detail, name='invoice-detail'),
    path('unpaid-invoices', invoice_unpaid, name='invoice-unpaid'),
    path('paid-invoices', invoice_paid, name='invoice-paid'),
    path('invoices', invoice_list, name='invoice-list'),
    path('draft-invoices', invoice_draft, name='invoice-draft'),
    
    #ITEMS
    path('invoice/<int:id>/item/add/', OrderItemCreateView.as_view(), name='create_item'),
    path('invoice/<int:id>/<int:pk>/update/', OrderItemUpdateView.as_view(), name='update_item'),
    path('invoice/<int:id>/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='delete_item'),
    path('invoice/<int:invoice_id>/update/', update_invoice, name='update-invoice'),
    path('invoice/<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),
    path('invoice/<int:invoice_id>/print/', printable_invoice, name='print-invoice'),
    path('invoice/<int:invoice_id>/download/', GeneratePdf.as_view(), name='download-invoice'), 
]