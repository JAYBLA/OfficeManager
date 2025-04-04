from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import View  # pdf download
from django.http import  HttpResponse
from django.conf import settings
from .models import Receipt
from .forms import ReceiptForm

from customer.models import Customer
from .utils import render_to_pdf

from datetime import datetime,timedelta,date
base_url = settings.BASE_URL

def receipt_list(request):
    receipts = Receipt.objects.all().order_by('-date')
    template_name = 'receipts/receipt_list.html'
    heading = "Receipts"
    context={
        'receipts':receipts,
        'heading':heading
    }
    return render(request, template_name, context)

def save_receipt_form(request,form,template_name):
    data=dict()
    if request.method == "POST":        
        if form.is_valid:
            form.save()
            data['form_is_valid']=True
            receipts = Receipt.objects.all().order_by('-date')
            data['html_receipt_list'] = render_to_string('receipts/includes/receipt_list_body.html', {
                'receipts': receipts
            })
        else:
            data['form_is_valid']=False
    else:        
        context = {'form': form}        
        html_receipt_form = render_to_string(template_name,context,request=request)
        data = {'html_receipt_form':html_receipt_form,}
    return JsonResponse(data)

def receipt_create(request):    
    if request.method == "POST":
        form = ReceiptForm(request.POST)
    else:
        form = ReceiptForm()       
    return save_receipt_form(request, form, 'receipts/receipt_create_form.html')


def receipt_update(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES, instance=receipt)
    else:
        form = ReceiptForm(instance=receipt)
    return save_receipt_form(request, form, 'receipts/receipt_update_form.html')

def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    data = dict()
    if request.method == 'POST':
        receipt.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        receipts = Receipt.objects.all()
        data['html_receipt_list'] = render_to_string('receipts/includes/receipt_list_body.html', {
            'receipts': receipts
        })
    else:
        context = {'receipt': receipt}
        data['html_receipt_form'] = render_to_string('receipts/receipt_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

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
        pdf = render_to_pdf('receipts/receipt-pdf-template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
