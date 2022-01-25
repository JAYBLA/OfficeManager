from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from quotation.models import Quotation
from customer.models import Customer
from invoice.models import Invoice
from django.conf import settings

base_url = settings.BASE_URL

# Create your views here.
@login_required()
def dashboard(request):
    template = 'home.html'
    invoices = Invoice.objects.all().order_by('-date')
    customers = Customer.objects.all().order_by('name')
    quotations = Quotation.objects.all().order_by('-date')    
    customer_count = customers.count()
    invoice_count = invoices.count()
    quotation_count = quotations.count()
    context = {			
        'invoices' : invoices,
        'customers' : customers,
        'quotations':quotations,
        'invoice_count':invoice_count,
        'customer_count':customer_count,
        'quotation_count':quotation_count,		
    }
    return render(request,template,context)

