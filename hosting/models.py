from django.db import models
from customer.models import Customer

class Hosting(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='hostings')
    domain = models.CharField(max_length=255)
    registration_date = models.DateField()
    expiring_date = models.DateField()
    domain_cost = models.DecimalField(max_digits=10, decimal_places=0)
    hosting_cost = models.DecimalField(max_digits=10, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.domain} ({self.customer.name})"

