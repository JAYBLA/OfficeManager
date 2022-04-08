from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'quotation'

urlpatterns = [    
    path('new/', quotation_create, name='new-quotation'),    
    path('<int:id>/', quotation_detail, name='quotation-detail'),
    path('copy/<int:quotation_id>/', quotation_copy, name='quotation-copy'),
    path('quotations', quotation_list, name='quotation-list'),
    
    path('<int:id>/item/add/', OrderItemCreateView.as_view(), name='create_item'),
    path('<int:id>/<int:pk>/update/', OrderItemUpdateView.as_view(), name='update_item'),  #ITEMS
    path('<int:id>/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='delete_item'),
    
    path('<int:id>/update/', update_quotation, name='update-quotation'),
    path('<int:pk>/delete/', QuotationDeleteView.as_view(), name='delete_quotation'),
    
                            #Sending Quotation
    path('<int:quotation_id>/send1/', send_quotationjaybla, name='send-quotation1'),
    path('<int:quotation_id>/send2/', send_quotationrare, name='send-quotation2'),
    path('<int:quotation_id>/send3/', send_quotationbafro, name='send-quotation3'),
    
    
                            #Downloading Quotation
    path('<int:quotation_id>/download1/', GeneratePdf1.as_view(), name='download-quotation1'),
    path('<int:quotation_id>/download2/', GeneratePdf2.as_view(), name='download-quotation2'),  
    path('<int:quotation_id>/download3/', GeneratePdf3.as_view(), name='download-quotation3'),    
]