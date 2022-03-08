from django.db import models
from customer.models import Customer

class Receipt(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    receipt_file = models.FileField(upload_to='receipts/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=False)
    amount = models.CharField(max_length=200)
    status=models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

