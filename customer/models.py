from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Customer(models.Model):    
    name                = models.CharField(max_length=150,unique=True)
    phone               = models.CharField(max_length=15, blank=True,null=True)
    email               = models.EmailField(max_length=150, blank=True,null=True)
    physical_address    = models.CharField(max_length=150)
    whatsapp_number = PhoneNumberField(
        region='TZ',  # optional default country for validation
        help_text='Enter WhatsApp number with country code.',
        blank=True,  # allow blank field
        null=True,  # allow null value
    )
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_at         = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
