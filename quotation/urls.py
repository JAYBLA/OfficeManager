from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'quotation'

urlpatterns = [    
    path('quotation/new/', quotation_create, name='new-quotation'),    
    path('quotation/<int:id>/', quotation_detail, name='quotation-detail'),
    path('quotations', quotation_list, name='quotation-list'),
    
    path('quotation/<int:id>/item/add/', OrderItemCreateView.as_view(), name='create_item'),
    path('quotation/<int:id>/<int:pk>/update/', OrderItemUpdateView.as_view(), name='update_item'),  #ITEMS
    path('quotation/<int:id>/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='delete_item'),
    
    path('quotation/<int:id>/update/', update_quotation, name='update-quotation'),
    path('quotation/<int:pk>/delete/', QuotationDeleteView.as_view(), name='delete_quotation'),
    path('quotation/<int:quotation_id>/print/', printable_quotation, name='print-quotation'),
    path('quotation/<int:quotation_id>/download/', GeneratePdf.as_view(), name='download-quotation'),  
]