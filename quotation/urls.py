from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'quotation'

urlpatterns = [    
    path('new/', quotation_create, name='new-quotation'),    
    path('<int:id>/', quotation_detail, name='quotation-detail'),
    path('quotations', quotation_list, name='quotation-list'),
    
    path('<int:id>/item/add/', OrderItemCreateView.as_view(), name='create_item'),
    path('<int:id>/<int:pk>/update/', OrderItemUpdateView.as_view(), name='update_item'),  #ITEMS
    path('<int:id>/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='delete_item'),
    
    path('<int:id>/update/', update_quotation, name='update-quotation'),
    path('<int:pk>/delete/', QuotationDeleteView.as_view(), name='delete_quotation'),
    path('<int:quotation_id>/print/', printable_quotation, name='print-quotation'),
    path('<int:quotation_id>/download/', GeneratePdf.as_view(), name='download-quotation'),  
]