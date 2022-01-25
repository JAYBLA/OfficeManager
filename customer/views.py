from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from bootstrap_modal_forms.generic import (
  BSModalDeleteView,
  BSModalUpdateView,
  BSModalCreateView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.urls import reverse_lazy


from .models import *
from quotation.models import Quotation

from datetime import datetime,timedelta,date
from .forms import *
from django.conf import settings

base_url = settings.BASE_URL

# Create your views here.
class CustomerCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'customer/customer-create.html'
    form_class = CustomerForm
    success_message = 'Created Successfully'
    
    def get_success_url(self):
        return reverse_lazy('customer:customer-list') 
    
class CustomerDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = Customer
    template_name = 'customer/delete.html'
    success_message = 'Success: Customer was deleted.'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer:customer-create')
    
class CustomerUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Customer
    template_name = 'customer/customer-update.html'
    form_class = CustomerForm
    success_message = 'Customer Updated Successfully.'
    
    def get_success_url(self):
        return reverse_lazy('customer:customer-list') 
    
    
@login_required()
def customer_detail(request,customer_id):
    template = 'customer/customer-detail.html'    
    customer = get_object_or_404(Customer, pk =customer_id)
    customers = Customer.objects.order_by('-modified_at')
    context = {
        'customer' :customer,
        'customers':customers,
    }
    
    return render(request, template,context)


@login_required()
def customer_list(request):
    template = 'customer/customer-list.html'    
    customers = Customer.objects.order_by('-modified_at')
    context = {        
        'customers':customers,
        'title':'All Customers'
    }
    
    return render(request, template,context)


@login_required()
def update_customer(request, customer_id):
    template = 'customer/customer-create-list.html'
    c = get_object_or_404(Customer, pk=customer_id)

    c.name = request.POST['name']
    c.phone = request.POST['phone']
    c.email = request.POST['email']
    c.address = request.POST['physical_address']

    c.save()
    customers = Customer.objects.order_by('-modified_at')
    context = {
        'customers' : customers,
    }
    return render(request, template,context)




