from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'receipt'

urlpatterns = [    
    path('new/', ReceiptCreateView.as_view(), name='new-receipt'),    
    # path('quotation/<int:id>/', quotation_detail, name='quotation-detail'),
    path('list/', receipt_list, name='receipt-list'),    
    # path('quotation/<int:id>/update/', update_quotation, name='update-quotation'),
    # path('quotation/<int:pk>/delete/', QuotationDeleteView.as_view(), name='delete_quotation'),
    # path('quotation/<int:quotation_id>/print/', printable_quotation, name='print-quotation'),
    # path('quotation/<int:quotation_id>/download/', GeneratePdf.as_view(), name='download-quotation'),  
]