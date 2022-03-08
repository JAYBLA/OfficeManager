from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'receipt'

urlpatterns = [    
    path('new/', ReceiptCreateView.as_view(), name='new-receipt'), 
    path('list/', receipt_list, name='receipt-list'),    
    # path('receipt/<int:id>/update/', update_receipt, name='update-receipt'),
    path('receipt/<int:pk>/delete/', ReceiptDeleteView.as_view(), name='delete_receipt'),
    path('receipt/<int:pk>/update/', ReceiptUpdateView.as_view(), name='update_receipt'),
    # path('receipt/<int:receipt_id>/print/', printable_receipt, name='print-receipt'),
    path('receipt/<int:receipt_id>/download/', DownloadableReceipt.as_view(), name='download-receipt'),  
]