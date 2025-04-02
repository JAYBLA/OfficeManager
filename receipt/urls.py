from django.urls import path
from . import views

app_name = 'receipt'

urlpatterns = [
    path('list/', views.receipt_list, name='receipt_list'),
    path('create/', views.receipt_create, name='receipt_create'),
    path('update/<int:pk>/', views.receipt_update, name='receipt_update'),
    path('delete/<int:pk>/', views.receipt_delete, name='receipt_delete'),
]
