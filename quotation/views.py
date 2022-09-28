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
from .forms import *

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
from customer.models import Customer
from quotation.models import OrderItem as QuotationOrderItem
from .utils import render_to_pdf

from datetime import datetime,timedelta,date

base_url = settings.BASE_URL

@login_required()
def quotation_create(request):
    template = 'quotation/quotation-create-list.html'
    # If no customer_id is defined, create a new invoice
    if request.method=='POST':
        customer_id = request.POST['customer_id']        
        quote_title = request.POST['quote_title']
        quote_description = request.POST['quote_description']
        due_date = request.POST['due_date']
        
        if customer_id=='None':
            customers = Customer.objects.order_by('name')
            context = {
                'customer_list' : customers,
                'error_message' : 'Please select a customer.',
            }
            return render(request, template, context)
        else:
            customer = get_object_or_404(Customer, pk=customer_id)
            quotation = Quotation(customer=customer, date=date.today(),quote_title=quote_title,quote_description=quote_description, due_date=due_date)
            quotation.save()
            
            quotations = Quotation.objects.order_by('-date')
            customers = Customer.objects.order_by('name')
            context = {			
            'quotation_list' : quotations,
            'customer_list' : customers,		
            }
        return render(request, template, context) 
    else:
        quotations = Quotation.objects.order_by('-date')
        customers = Customer.objects.order_by('name')
        context = {			
            'quotation_list' : quotations,
            'customer_list' : customers,			
        }
        return render(request, template, context)


class QuotationDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = Quotation
    template_name = 'quotation/delete.html'
    success_message = 'Success: Quotaion was deleted.'
    context_object_name = 'quotation'
    success_url = reverse_lazy('quotation:quotation-list')
   


@login_required()
def update_quotation(request, id):
    quotation = get_object_or_404(Quotation, pk=id)
    template = 'quotation/quotation-detail.html'
    try:        
        quotation.quote_title = request.POST['quote_title']
        quotation.quote_description = request.POST['quote_description']
        quotation.due_date = datetime.strptime(request.POST['due_date'], "%m/%d/%Y")
        quotation.save()
    except (KeyError, Quotation.DoesNotExist):
        return render(request, template, {
            'quotation': quotation,
            'error_message': 'Not able to update invoice!',
        })
    else:
        return redirect(to='quotation:quotation-detail',id=id)


@login_required() 
def delete_item(request, quotationitem_id, invoice_id):

    item = get_object_or_404(OrderItem, pk=quotationitem_id)
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    template = 'quotation/quotation-detail.html'
    try:
        item.delete()
    except (KeyError, QuotationItem.DoesNotExist):
        return render(request, template, {
            'quotation': quotation,
            'error_message': 'Item does not exist.',
        })
    else:
        return redirect(to='quotation:quotation-detail',id=quotation_id)


@login_required()
def quotation_detail(request, id):
    template = 'quotation/quotation-detail.html'
    quotation = get_object_or_404(Quotation, pk=id)   

    context = {      
        'quotation' : quotation,       
    }
    return render(request, template, context)

@login_required()
def quotation_list(request):
    template = 'quotation/quotation-list.html'
    quotations=Quotation.objects.all().order_by('-date')
    context = {			
        'quotation_list':quotations,		
    }
    return render(request, template, context)


class OrderItemCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'quotation/add_order_item_form.html'
    form_class = OrderItemForm
    success_message = 'Added Successfully'
    
    def get_success_url(self):
        return reverse_lazy('quotation:quotation-detail', kwargs={ "id": self.kwargs['id'] })    
    
    
    def form_valid(self, form):
        quotation_id = self.kwargs['id']
        form.instance.quotation_id = quotation_id
        return super().form_valid(form)
 

class OrderItemUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = OrderItem
    template_name = 'quotation/update_order_item_form.html'
    form_class = OrderItemForm
    success_message = 'Item Updated Successfully.'
    
    def get_success_url(self):
        return reverse_lazy('quotation:quotation-detail', kwargs={ "id": self.kwargs['id'] })  
   
class OrderItemDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = OrderItem
    template_name = 'quotation/delete_item.html'
    success_message = 'Success, Item was deleted.'
    context_object_name = 'item'
    
    def get_success_url(self):
        return reverse_lazy('quotation:quotation-detail', kwargs={ "id": self.kwargs['id'] })  


@login_required()
def send_quotationjaybla(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    email = quotation.customer.email
    customer = quotation.customer.name
    c=customer.upper()
    quotation_no = 'JB100R' + str(quotation.customer.id)+str(c[0]+str(c[1])+str(c[2])+"Q")
          
    data = {
        'quotation':quotation,
        'quotation_no':quotation_no,
        'created_at':quotation.date,
        'base_url':base_url,
    }
    
    pdf = render_to_pdf('quotation/quotation-pdf-templatejaybla.html', data)

    quotation.quotation_file.save(str(datetime.now())+'quotation.pdf', File(BytesIO(pdf.content)))
    
    try:
        mail = EmailMessage('JAYBLA GROUP', "Find the attachment of a quotation below", to=[email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.attach('quotation.pdf', pdf.getvalue(), 'application/pdf')
        mail.send()

        messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

        return redirect(to='quotation:quotation-list')
    except:
        messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

    return redirect(to='quotation:quotation-list')

@login_required()
def send_quotationrare(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    email = quotation.customer.email
    customer = quotation.customer.name
    c=customer.upper()
    quotation_no = 'JB100R' + str(quotation.customer.id)+str(c[0]+str(c[1])+str(c[2])+"Q")
          
    data = {
        'quotation':quotation,
        'quotation_no':quotation_no,
        'created_at':quotation.date,
        'base_url':base_url,
    }
    
    pdf = render_to_pdf('quotation/quotation-pdf-templaterare.html', data)

    quotation.quotation_file.save(str(datetime.now())+'quotation.pdf', File(BytesIO(pdf.content)))
    
    try:
        mail = EmailMessage('JAYBLA GROUP', "Find the attachment of a quotation below", to=[email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.attach('quotation.pdf', pdf.getvalue(), 'application/pdf')
        mail.send()

        messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

        return redirect(to='quotation:quotation-list')
    except:
        messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

    return redirect(to='quotation:quotation-list')

@login_required()
def send_quotationbafro(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    email = quotation.customer.email
    customer = quotation.customer.name
    c=customer.upper()
    quotation_no = 'JB100R' + str(quotation.customer.id)+str(c[0]+str(c[1])+str(c[2])+"Q")
          
    data = {
        'quotation':quotation,
        'quotation_no':quotation_no,
        'created_at':quotation.date,
        'base_url':base_url,
    }
    
    pdf = render_to_pdf('quotation/quotation-pdf-templatebafro.html', data)

    quotation.quotation_file.save(str(datetime.now())+'quotation.pdf', File(BytesIO(pdf.content)))
    
    try:
        mail = EmailMessage('JAYBLA GROUP', "Find the attachment of a quotation below", to=[email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.attach('quotation.pdf', pdf.getvalue(), 'application/pdf')
        mail.send()

        messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

        return redirect(to='quotation:quotation-list')
    except:
        messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

    return redirect(to='quotation:quotation-list')


@login_required()
def download_quotation(request,quotation_id):
    quote=get_object_or_404(Quotation, pk=quotation_id)
    if request.method == 'POST':
        if 'rare' in request.POST:
            template_name = 'quotation/quotation-pdf-templaterare.html'            
            quotation = generate_pdf(request, template_name, quotation_id)
            return quotation           
        elif 'bafro' in request.POST:
            template_name = 'quotation/quotation-pdf-templatebafro.html'
            quotation = generate_pdf(request, template_name, quotation_id)
            return quotation           
        else:
            if quote.orderitem_set.count()>=9:
                template_name = 'quotation/quotation-pdf-multijaybla.html'
            else:
                template_name = 'quotation/quotation-pdf-templatejaybla.html'
            quotation = generate_pdf(request, template_name, quotation_id)
            return quotation 

@login_required()
def generate_pdf(request,template_name,quotation_id):
    print("template_name", template_name)
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    customer = quotation.customer.name
    c=customer.upper()
    quotation_no = 'JB100R' + str(quotation.id)+str(c[0]+str(c[1])+str(c[2]))       
    data = {
        'quotation':quotation,
        'quotation_no':quotation_no,
        'created_at':quotation.date,
        'base_url':base_url,
    }
    pdf = render_to_pdf(template_name, data)
    return HttpResponse(pdf, content_type='application/pdf')




@login_required()
def quotation_copy(request,quotation_id):
    if request.method =='POST': 
     
        customer_id=request.POST.get('customer_id')    
        customer=get_object_or_404(Customer, id=customer_id)
        quotation = get_object_or_404(Quotation, pk=quotation_id)
        copied_quotation = Quotation(customer=customer, date=date.today(),quote_title=quotation.quote_title,quote_description=quotation.quote_description, due_date=quotation.due_date)
        copied_quotation.save()

        quotation_items =QuotationOrderItem.objects.filter(quotation_id=quotation_id)    
        for item in quotation_items:
            orderitem = OrderItem(description=item.description,cost=item.cost,qty=item.qty,quotation_id=copied_quotation.id)
            orderitem.save()
        return redirect(to='quotation:quotation-list')
    else:
        quotations = Quotation.objects.order_by('-date')
        customers = Customer.objects.order_by('name')
        context = {			
        'quotation_list' : quotations,
        'customer_list' : customers,		
        }
        return render(request,'quotation/quotation-copy.html',context)