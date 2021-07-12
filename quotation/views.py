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
from invoice.models import Customer
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
    success_url = reverse_lazy('quotation:new-quotation')
   


@login_required()
def update_quotation(request, id):
    quotation = get_object_or_404(Quotation, pk=id)
    template = 'quotation/quotation-detail.html'
    try:        
        quotation.quote_title = request.POST['quote_title']
        quotation.quote_description = request.POST['quote_description']
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
def add_order_item(request, id):
    quotation = get_object_or_404(Quotation, pk=id)
    try:
        order_item = quotation.orderitem_set.create(description=request.POST['description'], cost=request.POST['cost'], qty=request.POST['qty'])
        order_item.save()
    except (KeyError, Quotation.DoesNotExist):
        return render(request, 'quotation/quotation-detail.html', {
            'quotation': quotation,
            'error_message': 'Not all fields were completed.',
        })
    else:
        return redirect('quotation:quotation-detail',id=id)
    

@login_required()
def printable_quotation(request, quotation_id):
    quotation = get_object_or_404(Quotation, pk=quotation_id)
    email = quotation.customer.email
    customer = quotation.customer.name
    c=customer.upper()
    quotation_no = 'JG100' + str(quotation.customer.id)+str(c[0]+str(c[1])+str(c[2])+"Q")
          
    data = {
        'quotation':quotation,
        'quotation_no':quotation_no,
        'created_at':quotation.date,
        'base_url':base_url,
    }
    
    pdf = render_to_pdf('quotation/quotation-pdf-template.html', data)

    quotation.quotation_file.save(str(datetime.now())+'quotation.pdf', File(BytesIO(pdf.content)))
    
    try:
        mail = EmailMessage('JAYBLA GROUP MANAGEMENT', "Find the attachment of a quotation below", to=[email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.attach('quotation.pdf', pdf.getvalue(), 'application/pdf')
        mail.send()

        messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

        return redirect(to='invoice:app-home')
    except:
        messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

    return redirect(to='invoice:app-home')


@method_decorator(login_required, name='dispatch')
class GeneratePdf(View):
    def get(self,request, quotation_id):
        quotation = get_object_or_404(Quotation, pk=quotation_id)
        customer = quotation.customer.name
        c=customer.upper()
        quotation_no = 'JG100' + str(quotation.customer.id)+str(c[0]+str(c[1])+str(c[2]) + 'Q')
        due_date = datetime.today() + timedelta(days=5)


        data = {
            'quotation':quotation,
            'quotation_no':quotation_no,
            'created_at':quotation.date,
            'due_date':due_date,
            'base_url':base_url,
        }
        pdf = render_to_pdf('quotation/quotation-pdf-template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
