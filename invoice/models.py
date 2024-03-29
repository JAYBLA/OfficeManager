from django.db import models
from customer.models import Customer
from .choices import INVOICE_CATEGORIES,INVOICE_TYPE


# Create your models here.
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    category=models.CharField(max_length=10,choices=INVOICE_CATEGORIES, default='others')
    invoice_type = models.CharField(max_length=10,choices=INVOICE_TYPE, default='proforma')
    status = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    send_date = models.DateTimeField(null=True, blank=True)
    invoice_file = models.FileField(upload_to='invoices/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def total_items(self):
        total = 0
        items = self.orderitem_set.all()

        for item in items:
            total += item.cost * item.qty

        return total


    def total(self):
        items = self.total_items()
        return items
        
    def paid(self):
        return self.status == 'Paid'
        
    def unpaid(self):
        return self.status == 'Unpaid'
        
    def draft(self):
        return self.status == 'Draft'    


class OrderItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.IntegerField()
    qty = models.IntegerField()

    def total(self):
        return self.cost * self.qty