from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Receipt
from .forms import ReceiptForm

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
    if request.method == 'POST':
        receipt.delete()
        return redirect('receipt_list')
    return render(request, 'receipts/receipt_confirm_delete.html', {'receipt': receipt})
