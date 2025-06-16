from django.urls import path
from . import views

app_name = 'hosting'

urlpatterns = [
    path('list/', views.hosting_list, name='hosting_list'),
    path('create/', views.hosting_create, name='hosting_create'),
    path('<int:pk>/edit/', views.hosting_edit, name='hosting_edit'),
    path('<int:pk>/delete/', views.hosting_delete, name='hosting_delete'),
    path('download-invoice/', views.download_invoice, name='download_invoice'),
]
