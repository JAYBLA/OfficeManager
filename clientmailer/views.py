from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

from .forms import *

base_url = settings.BASE_URL

@login_required()
def mail_list(request):
    template = 'clientmailer/mail_list.html'    
    mails = ClientMail.objects.order_by('-modified_at')
    context = {       
        
        'title':'Client Mails Sent',
        'mails':mails,
    }
    
    return render(request, template,context)

class ClientMailCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'clientmailer/new_mail.html'
    form_class = ClientMailForm
    success_message = 'Created Successfully'
    
    def get_success_url(self):
        return reverse_lazy('clientmailer:clientmail-list')

class ClientMailDeleteView(LoginRequiredMixin,BSModalDeleteView):
    model = ClientMail
    template_name = 'clientmailer/delete.html'
    success_message = 'Successfully deleted.'
    context_object_name = 'm'
    success_url = reverse_lazy('clientmailer:clientmail-list')
    
class ClientMailUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = ClientMail
    template_name = 'clientmailer/update_mail.html'
    form_class = ClientMailForm
    success_message = 'Updated Successfully.'
    
    def get_success_url(self):
        return reverse_lazy('clientmailer:clientmail-list')  

@login_required()
def send_client_mail(request, mail_id):
    client_mail = get_object_or_404(ClientMail, pk=mail_id)
    recipient_email = client_mail.customer.email
    mail_subject = client_mail.subject 
    mail_content = client_mail.content
    client = client_mail.customer.name

    data = {
        'mail_content': mail_content,
        'client':client,
    }
    mail_template = render_to_string("clientmailer/client-mail-template.html", data)

    
    subject = mail_subject
    text_content = client_mail.content
    from_email='info@jayblagroup.co.tz'
    to = recipient_email 

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(mail_template, "text/html")
    msg.send()
    return redirect( to="clientmailer:clientmail-list")


