from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'receipt'

urlpatterns = [    
    path('new/', ReceiptCreateView.as_view(), name='new-receipt'), 
    path('list/', receipt_list, name='receipt-list'), 
    path('receipt/<int:pk>/delete/', ReceiptDeleteView.as_view(), name='delete_receipt'),
    path('receipt/<int:pk>/update/', ReceiptUpdateView.as_view(), name='update_receipt'),
    path('<int:receipt_id>/send1/', send_receipt, name='send-receipt'),
    path('receipt/<int:receipt_id>/download/', DownloadableReceipt.as_view(), name='download-receipt'),  
]