from django.db import models

# Create your models here.
class Customer(models.Model):    
    name                = models.CharField(max_length=150,unique=True)
    phone               = models.CharField(max_length=15)
    email               = models.EmailField(max_length=150)
    physical_address    = models.CharField(max_length=150)
    created_at          = models.DateTimeField(auto_now_add=True)
    modified_at         = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)
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