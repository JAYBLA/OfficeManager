from django.db import models
from customer.models import Customer


# Create your models here.
class ClientMail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subject    = models.CharField(max_length=150)
    content = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)   
    






