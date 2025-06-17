from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Hosting
from .forms import HostingForm
from django.http import HttpResponse
from django.template.loader import render_to_string


#  List all hosting records
def hosting_list(request):
    hostings = Hosting.objects.all()
    return render(request, 'hosting/hosting_list.html', {'hostings': hostings})

def hosting_create(request):
    if request.method == 'POST':
        form = HostingForm(request.POST)
        if form.is_valid():
            hosting = form.save()
            return JsonResponse({'success': True, 'id': hosting.id})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = HostingForm()
        return render(request, 'hosting/partials/hosting_form.html', {'form': form})

def hosting_edit(request, pk):
    hosting = get_object_or_404(Hosting, pk=pk)
    if request.method == 'POST':
        form = HostingForm(request.POST, instance=hosting)
        if form.is_valid():
            hosting = form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = HostingForm(instance=hosting)
        return render(request, 'hosting/partials/hosting_form.html', {'form': form, 'edit': True, 'pk': pk})

def hosting_delete(request, pk):
    hosting = get_object_or_404(Hosting, pk=pk)
    if request.method == 'POST':
        hosting.delete()
        return JsonResponse({'success': True})
    return render(request, 'hosting/partials/hosting_confirm_delete.html', {'object': hosting})


def download_invoice(request):
    # 1. Render the HTML template with context
    html_string = render_to_string("hosting/invoice.html", {
        'invoice_number': 'JB100R1JUM',
        'customer_name': 'Jumanne Joseph',
        'total': 330000,
        # Add other context as needed
    })

    # 2. Convert HTML to PDF
    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()

    # 3. Return the response as a downloadable file
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response
