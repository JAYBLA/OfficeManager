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
from .utils import render_to_pdf

from datetime import datetime,timedelta,date

base_url = settings.BASE_URL

@login_required()
def receipt_list(request):
    template = 'receipt/receipt-list.html'
    receipts=Receipt.objects.all().order_by('-date')
    customers = Customer.objects.order_by('name')

    context = {			
        'receipt_list':receipts,
        'customer_list' : customers,		
    }
    return render(request, template, context)

class ReceiptCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'receipt/create_receipt_form.html'
    form_class = ReceiptForm
    success_message = 'Added Successfully'
    
    def get_success_url(self):
        return reverse_lazy('receipt:receipt-list')    

 
 


# @login_required()
# def printable_receipt(request, receipt_id):
#     receipt = get_object_or_404(receipt, pk=receipt_id)
#     email = receipt.customer.email
#     customer = receipt.customer.name
#     c=customer.upper()
#     receipt_no = 'JG100' + str(receipt.customer.id)+str(c[0]+str(c[1])+str(c[2])+"Q")
          
#     data = {
#         'receipt':receipt,
#         'receipt_no':receipt_no,
#         'created_at':receipt.date,
#         'base_url':base_url,
#     }
    
#     pdf = render_to_pdf('receipt/receipt-pdf-template.html', data)

#     receipt.receipt_file.save(str(datetime.now())+'receipt.pdf', File(BytesIO(pdf.content)))
    
#     try:
#         mail = EmailMessage('JAYBLA GROUP MANAGEMENT', "Find the attachment of a receipt below", to=[email], from_email=settings.EMAIL_HOST_USER)
#         mail.content_subtype = 'html'
#         mail.attach('receipt.pdf', pdf.getvalue(), 'application/pdf')
#         mail.send()

#         messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

#         return redirect(to='invoice:app-home')
#     except:
#         messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

#     return redirect(to='invoice:app-home')


@method_decorator(login_required, name='dispatch')
class DownloadableReceipt(View):
    def get(self,request, receipt_id):
        receipt = get_object_or_404(Receipt, pk=receipt_id)
        customer = receipt.customer.name
        c=customer.upper()
        receipt_no = 'JB100R' + str(receipt.customer.id)+str(c[0]+str(c[1])+str(c[2]) + 'Q')
        
        data = {
            'receipt':receipt,
            'receipt_no':receipt_no,
            'created_at':receipt.date,
            'base_url':base_url,
        }
        pdf = render_to_pdf('receipt/receipt-pdf-template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

