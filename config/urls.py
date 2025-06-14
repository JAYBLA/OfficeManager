"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls', namespace='dashboard')),
    path('users/', include('users.urls', namespace='users')),
    path('quotation/', include('quotation.urls', namespace='quotation')),
    path('receipt/', include('receipt.urls', namespace='receipt')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('invoice/', include('invoice.urls', namespace='invoice')),
    path('clientmailer/', include('clientmailer.urls', namespace='clientmailer')),
    path('hosting/', include('hosting.urls', namespace='hosting')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)