from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from io import BytesIO
from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View  # pdf download
from django.http import  HttpResponse
from bootstrap_modal_forms.generic import (
  BSModalDeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.urls import reverse_lazy


from .models import *
from quotation.models import Quotation
from .utils import render_to_pdf

from datetime import datetime,timedelta,date

base_url = settings.BASE_URL

# Create your views here.
@login_required()
def home(request):
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

@login_required()
def customer_create(request):
    template = 'customer/customer-create-list.html'
    if request.method =='POST':
        customer = Customer(
            name = request.POST['full_name'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            physical_address = request.POST['physical_address']
        )
        
        customer.save()
        customers = Customer.objects.order_by('-created_at')
        
        data = {
            'customers':customers
        }
        return render(request,template,data)
    else:
        customers = Customer.objects.order_by('-created_at')
        data = {
            'customers':customers
        }
        
        return render(request,template,data)

class CustomerDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = Customer
    template_name = 'customer/delete.html'
    success_message = 'Success: Customer was deleted.'
    context_object_name = 'customer'
    success_url = reverse_lazy('invoice:customer-create-list')
    

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


@login_required()
def invoice_create(request):
    template = 'invoice/invoice-create-list.html'
    # If no customer_id is defined, create a new invoice
    if request.method=='POST':
        customer_id = request.POST['customer_id']
        due_date = request.POST['due_date']
        title = request.POST['title']
                
        if customer_id=='None':
            customers = Customer.objects.order_by('name')
            context = {
                'customer_list' : customers,
                'error_message' : 'Please select a customer.',
            }
            return render(request, template, context)
        else:
            customer = get_object_or_404(Customer, pk=customer_id)
            invoice = Invoice(customer=customer, date=date.today(), status='Unpaid', due_date=due_date, title=title)
            invoice.save()
            
            invoices = Invoice.objects.order_by('-date')
            customers = Customer.objects.order_by('name')
            context = {			
            'invoice_list' : invoices,
            'customer_list' : customers,		
            }
        return render(request, template, context) 
    else:
        invoices = Invoice.objects.order_by('-date')
        customers = Customer.objects.order_by('name')
        context = {			
            'invoice_list' : invoices,
            'customer_list' : customers,			
        }
        return render(request, template, context)


@login_required()
def invoice_list(request):
    template = 'invoice/invoice-list.html'    
    invoices = Invoice.objects.all().order_by('-date')
    title = 'All Invoices'
    context = {			
        'invoice_list' : invoices,
        'title':title,		
    }
    return render(request, template,context)


@login_required()
def invoice_unpaid(request):
    template = 'invoice/invoice-list.html'    
    invoices = Invoice.objects.filter(status='Unpaid').order_by('-date')
    title = 'Unpaid Invoice'
    context = {			
        'invoice_list' : invoices,
        'title':title,		
    }
    return render(request, template,context)

@login_required()
def invoice_paid(request):
    template = 'invoice/invoice-list.html'    
    invoices = Invoice.objects.filter(status='Paid').order_by('-date')
    title = 'Paid Invoice'
    context = {			
        'invoice_list' : invoices,
        'title':title,		
    }
    return render(request, template,context)

@login_required()
def invoice_draft(request):
    template = 'invoice/invoice-list.html'    
    invoices = Invoice.objects.filter(status='Draft').order_by('-date')
    title = 'Draft Invoice'
    context = {			
        'invoice_list' : invoices,
        'title':title,		
    }
    return render(request, template,context)

@login_required()
def update_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    template = 'invoice/invoice-detail.html'
    try:
        invoice.date = datetime.strptime(request.POST['date'], "%m/%d/%Y")
        invoice.due_date = datetime.strptime(request.POST['due_date'], "%m/%d/%Y")
        invoice.title = request.POST['title']
        invoice.status = request.POST['status']
        invoice.save()
    except (KeyError, Invoice.DoesNotExist):
        return render(request, template, {
            'invoice': invoice,
            'error_message': 'Not able to update invoice!',
        })
    else:
        return redirect(to='invoice:invoice-detail',id=invoice_id)

class InvoiceDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = Invoice
    template_name = 'invoice/delete.html'
    success_message = 'Success: Invoice was deleted.'
    context_object_name = 'invoice'
    success_url = reverse_lazy('invoice:new-invoice')
    
@login_required() 
def delete_item(request, invoiceitem_id, invoice_id):

    item = get_object_or_404(OrderItem, pk=invoiceitem_id)
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    template = 'invoice/invoice-detail.html'
    try:
        item.delete()
    except (KeyError, InvoiceItem.DoesNotExist):
        return render(request, template, {
            'invoice': invoice,
            'error_message': 'Item does not exist.',
        })
    else:
        return redirect(to='invoice:invoice-detail',id=invoice_id)


@login_required()
def invoice_detail(request, id):
    template = 'invoice/invoice-detail.html'
    invoice = get_object_or_404(Invoice, pk=id)
    context = {
        'title' : 'Invoice ' + str(id),
        'invoice' : invoice,
    }
    return render(request, template, context)


@login_required()
def add_order_item(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    try:
        order_item = invoice.orderitem_set.create(description=request.POST['description'], cost=request.POST['cost'], qty=request.POST['qty'])
        order_item.save()
    except (KeyError, Invoice.DoesNotExist):
        return render(request, 'invoice/invoice-detail.html', {
            'invoice': invoice,
            'error_message': 'Not all fields were completed.',
        })
    else:
        return redirect('invoice:invoice-detail',id=id)
    

@login_required()
def printable_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    email = invoice.customer.email
    customer = invoice.customer.name
    c=customer.upper()
    invoice_no = 'JGM100' + str(invoice.customer.id)+str(c[0]+str(c[1])+str(c[2]))
    due_date = invoice.due_date
      
    data = {
        'invoice':invoice,
        'invoice_no':invoice_no,
        'created_at':invoice.date,
        'due_date':due_date,
        'base_url':base_url,
    }
    
    pdf = render_to_pdf('invoice/pdf-template.html', data)

    invoice.invoice_file.save(str(datetime.now())+'invoice.pdf', File(BytesIO(pdf.content)))
    
    try:
        mail = EmailMessage('JAYBLA GROUP MANAGEMENT', "Find the invoice below", to=[email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.attach('invoice.pdf', pdf.getvalue(), 'application/pdf')
        mail.send()

        messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

        return redirect(to='invoice:app-home')
    except:
        messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

    return redirect(to='invoice:app-home')

@method_decorator(login_required, name='dispatch')
class GeneratePdf(View):
    def get(self,request, invoice_id):
        invoice = get_object_or_404(Invoice, pk=invoice_id)
        customer = invoice.customer.name
        c=customer.upper()
        invoice_no = 'JGM100' + str(invoice.customer.id)+str(c[0]+str(c[1])+str(c[2]))

        data = {
            'invoice':invoice,
            'invoice_no':invoice_no,
            'created_at':invoice.date,
            'base_url':base_url,
        }
        pdf = render_to_pdf('invoice/pdf-template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
