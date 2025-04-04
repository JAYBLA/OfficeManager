from django.urls import path
from .views import *


app_name = 'receipt'

urlpatterns = [
    path('list/', receipt_list, name='receipt_list'),
    path('create/', receipt_create, name='receipt_create'),
    path('update/<int:pk>/', receipt_update, name='receipt_update'),
    path('delete/<int:pk>/', receipt_delete, name='receipt_delete'),
    path('receipt/<int:receipt_id>/download/', DownloadableReceipt.as_view(), name='download-receipt'),
]
