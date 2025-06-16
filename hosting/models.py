from django.db import models
from customer.models import Customer
from django.utils import timezone
from datetime import timedelta

class Hosting(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='hostings')
    domain = models.CharField(max_length=255)
    expiring_date = models.DateField()
    domain_cost = models.DecimalField(max_digits=10, decimal_places=0)
    hosting_cost = models.DecimalField(max_digits=10, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    last_notified = models.DateField(null=True, blank=True)
    next_due = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically set next_due = expiring_date + 1 year
        if self.expiring_date:
            self.next_due = self.expiring_date + timedelta(days=365)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.domain} ({self.customer.name})"

