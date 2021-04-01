from django.contrib import admin

from .models import Quotation,OrderItem

admin.site.register(Quotation)
admin.site.register(OrderItem)
