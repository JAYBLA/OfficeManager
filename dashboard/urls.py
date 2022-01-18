from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [  
    #CUSTOMER
    path('', dashboard, name='dashboard'),
]