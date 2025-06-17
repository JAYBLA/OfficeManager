from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'invoice'

urlpatterns = [
    #INVOICE
    path('invoice/new/', invoice_create, name='create-invoice'),
    path('invoice/new/<int:quotation_id>/', invoice_from_quotation, name='invoice-from-quotation'),    
    path('invoice/<int:id>/', invoice_detail, name='invoice-detail'),
    path('unpaid-invoices/', invoice_unpaid, name='invoice-unpaid'),
    path('paid-invoices/', invoice_paid, name='invoice-paid'),
    path('invoices/', invoice_list, name='invoice-list'),    
    path('draft-invoices/', invoice_draft, name='invoice-draft'),
    path('invoices/toggle-invoice-status/<int:invoice_id>/', toggle_invoice_status, name='toggle_invoice_status'),
    #ITEMS
    path('invoice/<int:id>/item/add/', OrderItemCreateView.as_view(), name='create_item'),
    path('invoice/<int:id>/<int:pk>/update/', OrderItemUpdateView.as_view(), name='update_item'),
    path('invoice/<int:id>/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='delete_item'),
    path('invoice/<int:invoice_id>/update/', update_invoice, name='update-invoice'),
    path('invoice/<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),
    
                        #SENDING INVOICE ATTACHMENTS
    path('invoice/<int:invoice_id>/send/', email_invoice, name='email-invoice'),
    
                        #DOWNLOAD INVOICE ATTACHMENTS
    path('invoice/<int:invoice_id>/download/', download_invoice, name='download-invoice'),    
]