from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'invoice'

urlpatterns = [
    #INVOICE
    path('invoice/new/', invoice_create, name='new-invoice'),
    path('invoice/new/<int:quotation_id>/', invoice_from_quotation, name='invoice-from-quotation'),    
    path('invoice/<int:id>/', invoice_detail, name='invoice-detail'),
    path('unpaid-invoices', invoice_unpaid, name='invoice-unpaid'),
    path('paid-invoices', invoice_paid, name='invoice-paid'),
    path('invoices', formal_invoice_list, name='formal_invoice_list'),
    path('proformainvoices', proforma_invoice_list, name='proforma_invoice_list'),
    path('draft-invoices', invoice_draft, name='invoice-draft'),
    
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