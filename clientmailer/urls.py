from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'clientmailer'

urlpatterns = [
    #INVOICE
    path('clientmailer/new/', ClientMailCreateView.as_view(), name='mail_create'),
    path('clientmailer/list/', mail_list, name='clientmail-list'),
    path('clientmailer/<int:pk>/update/', ClientMailUpdateView.as_view(), name='mail_update'),
    path('clientmailer/<int:pk>/delete/', ClientMailDeleteView.as_view(), name='mail_delete'),
    path('clientmailer/<int:mail_id>/send-mail/', send_client_mail, name='send_mail')
   
]