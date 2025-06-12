from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import *

  
class CustomerForm(BSModalModelForm):
	
	class Meta:
		model = Customer
		fields = ['name', 'phone', 'whatsapp_number', 'email', 'physical_address',]
