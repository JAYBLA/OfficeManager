from django.urls import path
from .views import *


app_name = 'receipt'

urlpatterns = [
    path('list/', receipt_list, name='receipt-list'),
    path('create/', receipt_create, name='create-receipt'),
    path('update/<int:pk>/', receipt_update, name='update-receipt'),
    path('delete/<int:pk>/', receipt_delete, name='delete-receipt'),
    path('receipt/<int:receipt_id>/download/', DownloadableReceipt.as_view(), name='download-receipt'),
]
