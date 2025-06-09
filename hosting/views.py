from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Hosting
from .forms import HostingForm

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