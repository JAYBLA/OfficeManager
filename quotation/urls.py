from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'quotation'

urlpatterns = [    
    path('quotation/new/', quotation_create, name='new-quotation'),    
    path('quotation/<int:id>/', quotation_detail, name='quotation-detail'),
    path('quotation/<int:id>/item/add/', add_order_item, name='add-item'),
    path('quotation/<int:quotation_id>/item/<int:quotationitem_id>/delete/', delete_item, name='delete-item'),
    path('quotation/<int:id>/update/', update_quotation, name='update-quotation'),
    path('quotation/<int:quotation_id>/print/', printable_quotation, name='print-quotation'),
    path('quotation/<int:quotation_id>/download/', GeneratePdf.as_view(), name='download-quotation'),  
]