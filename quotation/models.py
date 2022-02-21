from django.db import models
from invoice.models import Invoice
from customer.models import Customer



class Quotation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    date = models.DateField()
    quotation_file = models.FileField(upload_to='quotations/%Y/%m/%d/', blank=True, null=True)
    quote_title = models.TextField(blank=False)
    quote_description = models.TextField(blank=True)
    due_date = models.DateField()

    def __str__(self):
        return str(self.quote_title)

    def total_items(self):
        total = 0
        items = self.orderitem_set.all()

        for item in items:
            total += item.cost * item.qty

        return total


    def total(self):
        items = self.total_items()
        return items


class OrderItem(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.IntegerField()
    qty = models.IntegerField()

    def total(self):
        return self.cost * self.qty