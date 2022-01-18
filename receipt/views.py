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
# from .utils import render_to_pdf

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

 

# class OrderItemUpdateView(LoginRequiredMixin, BSModalUpdateView):
#     model = OrderItem
#     template_name = 'quotation/update_order_item_form.html'
#     form_class = OrderItemForm
#     success_message = 'Item Updated Successfully.'
    
#     def get_success_url(self):
#         return reverse_lazy('quotation:quotation-detail', kwargs={ "id": self.kwargs['id'] })  
   
# class OrderItemDeleteView(LoginRequiredMixin, BSModalDeleteView):
#     model = OrderItem
#     template_name = 'quotation/delete_item.html'
#     success_message = 'Success, Item was deleted.'
#     context_object_name = 'item'
    
#     def get_success_url(self):
#         return reverse_lazy('quotation:quotation-detail', kwargs={ "id": self.kwargs['id'] })  


# @login_required()
# def printable_quotation(request, quotation_id):
#     quotation = get_object_or_404(Quotation, pk=quotation_id)
#     email = quotation.customer.email
#     customer = quotation.customer.name
#     c=customer.upper()
#     quotation_no = 'JG100' + str(quotation.customer.id)+str(c[0]+str(c[1])+str(c[2])+"Q")
          
#     data = {
#         'quotation':quotation,
#         'quotation_no':quotation_no,
#         'created_at':quotation.date,
#         'base_url':base_url,
#     }
    
#     pdf = render_to_pdf('quotation/quotation-pdf-template.html', data)

#     quotation.quotation_file.save(str(datetime.now())+'quotation.pdf', File(BytesIO(pdf.content)))
    
#     try:
#         mail = EmailMessage('JAYBLA GROUP MANAGEMENT', "Find the attachment of a quotation below", to=[email], from_email=settings.EMAIL_HOST_USER)
#         mail.content_subtype = 'html'
#         mail.attach('quotation.pdf', pdf.getvalue(), 'application/pdf')
#         mail.send()

#         messages.success(request, 'Success, Invoice was Sent successfully', extra_tags='alert alert-success')

#         return redirect(to='invoice:app-home')
#     except:
#         messages.error(request, 'Something went wrong while sending an attachment!', extra_tags='alert alert-danger')

#     return redirect(to='invoice:app-home')


# @method_decorator(login_required, name='dispatch')
# class GeneratePdf(View):
#     def get(self,request, quotation_id):
#         quotation = get_object_or_404(Quotation, pk=quotation_id)
#         customer = quotation.customer.name
#         c=customer.upper()
#         quotation_no = 'JG100' + str(quotation.customer.id)+str(c[0]+str(c[1])+str(c[2]) + 'Q')
#         due_date = quotation.due_date


#         data = {
#             'quotation':quotation,
#             'quotation_no':quotation_no,
#             'created_at':quotation.date,
#             'due_date':due_date,
#             'base_url':base_url,
#         }
#         pdf = render_to_pdf('quotation/quotation-pdf-template.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

