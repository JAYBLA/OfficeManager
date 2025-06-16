from django import forms
from .models import Hosting

class HostingForm(forms.ModelForm):
    class Meta:
        model = Hosting
        exclude = ['last_notified','next_due']
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'expiring_date': forms.DateInput(attrs={'type': 'date'}),
        }

