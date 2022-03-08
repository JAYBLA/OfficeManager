from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import *
  
class ReceiptForm(BSModalModelForm):
	
	class Meta:
		model = Receipt
		fields = ['customer', 'date', 'description', 'amount','status',]