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

def receipt_create(request):
    data=dict()
    if request.method == "POST":
        form = ReceiptForm(request.POST)
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
        form = ReceiptForm()
        context = {'form': form}
        template_name = 'receipts/receipt_create_form.html'
        html_receipt_form = render_to_string(template_name,context,request=request)
        data = {'html_receipt_form':html_receipt_form,}
    return JsonResponse(data)


def receipt_update(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('receipt_list')
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, 'receipts/receipt_form.html', {'form': form})

def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == 'POST':
        receipt.delete()
        return redirect('receipt_list')
    return render(request, 'receipts/receipt_confirm_delete.html', {'receipt': receipt})
