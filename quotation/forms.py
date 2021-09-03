from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import *



class OrderItemForm(BSModalModelForm):
	
	class Meta:
		model = OrderItem
		fields = ['description', 'cost', 'qty',]