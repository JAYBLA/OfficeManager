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
from quotation.models import OrderItem as QuotationOrderItem
from customer.models import Customer
from .utils import render_to_pdf
from datetime import datetime,timedelta,date
from .forms import *

base_url = settings.BASE_URL

# Create your views here.
@login_required()
def invoice_create(request):
    template = 'invoice/invoice-create-list.html'
    # If no customer_id is defined, create a new invoice
    if request.method=='POST':
        customer_id = request.POST['customer_id']
        due_date = request.POST['due_date']
        title = request.POST['title']
        invoice_type = request.POST['type']
        category = request.POST['category']
                
        if customer_id=='None':
            customers = Customer.objects.order_by('name')
            context = {
                'customer_list' : customers,
                'error_message' : 'Please select a customer.',
            }
            return render(request, template, context)
        else:
            customer = get_object_or_404(Customer, pk=customer_id)
            invoice = Invoice(customer=customer, date=date.today(), status='Unpaid', due_date=due_date, title=title, category=category, invoice_type=invoice_type)
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
        invoice.category = request.POST['category']
        invoice.invoice_type = request.POST['type']
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
    success_url = reverse_lazy('invoice:invoice_list')
    

@login_required()
def invoice_detail(request, id):
    template = 'invoice/invoice-detail.html'
    invoice = get_object_or_404(Invoice, pk=id)
    context = {
        'title' : 'Invoice ' + str(id),
        'invoice' : invoice,
    }
    return render(request, template, context)

    
class OrderItemCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'invoice/add_order_item_form.html'
    form_class = OrderItemForm
    success_message = 'Added Successfully'
    
    def get_success_url(self):
        return reverse_lazy('invoice:invoice-detail', kwargs={ "id": self.kwargs['id'] })    
    
    
    def form_valid(self, form):
        invoice_id = self.kwargs['id']
        form.instance.invoice_id = invoice_id
        return super().form_valid(form)
 

class OrderItemUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = OrderItem
    template_name = 'invoice/update_order_item_form.html'
    form_class = OrderItemForm
    success_message = 'Item Updated Successfully.'
    
    def get_success_url(self):
        return reverse_lazy('invoice:invoice-detail', kwargs={ "id": self.kwargs['id'] })  
   
class OrderItemDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = OrderItem
    template_name = 'invoice/delete_item.html'
    success_message = 'Success, Item was deleted.'
    context_object_name = 'item'
    
    def get_success_url(self):
        return reverse_lazy('invoice:invoice-detail', kwargs={ "id": self.kwargs['id'] })  


@login_required()
def email_invoice(request, invoice_id):
    template_name = 'invoice/pdf-invoicejaybla.html'
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    email_body = 'Please find the attachment of invoice on' + ' ' + str(invoice.title)
    email = invoice.customer.email
    customer = invoice.customer.name
    invoice_type = invoice.invoice_type
    if invoice_type == 'formal':
        invoice_head = 'invoice'
    else:
        invoice_head = 'proforma invoice'
    c=customer.upper()
    invoice_no = 'JB100R' + str(invoice.customer.id)+str(c[0]+str(c[1])+str(c[2]))
    due_date = invoice.due_date
      
    data = {
        'invoice':invoice,
        'invoice_no':invoice_no,
        'created_at':invoice.date,
        'invoice_type':invoice_head,
        'due_date':due_date,
        'base_url':base_url,
    }
    
    pdf = render_to_pdf(template_name, data)

    invoice.invoice_file.save(str(datetime.now())+'invoice.pdf', File(BytesIO(pdf.content)))
    
    try:
        mail = EmailMessage('JAYBLA GROUP', email_body, from_email='info@jayblagroup.co.tz' , to=[email], )
        mail.content_subtype = 'html'
        mail.attach('invoice.pdf', pdf.getvalue(), 'application/pdf')
        mail.send()

        messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

        return redirect(to='invoice:invoice_list')
    except:
        messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

    return redirect(to='invoice:invoice_list')


@login_required()
def download_invoice(request,invoice_id):
    template_name = 'invoice/pdf-invoicejaybla.html'    
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice_type = invoice.invoice_type
    if invoice_type == 'formal':
        invoice_head = 'invoice'
    else:
        invoice_head = 'proforma invoice'
    customer = invoice.customer.name
    c=customer.upper()
    invoice_no = 'JB100R' + str(invoice.customer.id)+str(c[0]+str(c[1])+str(c[2]))       
    data = {
        'invoice':invoice,
        'invoice_no':invoice_no,
        'created_at':invoice.date,
        'invoice_type':invoice_head,
        'base_url':base_url,
    }
    pdf = render_to_pdf(template_name, data)
    return HttpResponse(pdf, content_type='application/pdf')


@login_required()
def invoice_from_quotation(request,quotation_id):    
    quotation=get_object_or_404(Quotation, id=quotation_id)
    customer=get_object_or_404(Customer, name=quotation.customer.name)
    invoice = Invoice(customer=customer, date=date.today(), status='Unpaid', due_date=quotation.due_date)
    invoice.save()
    quotation_items =QuotationOrderItem.objects.filter(quotation_id=quotation_id)
    for item in quotation_items:
        orderitem = OrderItem(description=item.description,cost=item.cost,qty=item.qty,invoice_id=invoice.id)
        orderitem.save()
    return redirect(to='invoice:invoice_list')
    