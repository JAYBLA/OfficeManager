from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import *

  
class ClientMailForm(BSModalModelForm):
	
	class Meta:
		model = ClientMail
		fields = ['customer', 'subject', 'content',]
