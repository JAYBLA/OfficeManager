from django.core.management.base import BaseCommand
from django.utils import timezone
from hosting.models import Hosting  # replace with your app name
from notifications.utils import send_expiry_notification

class Command(BaseCommand):
    help = 'Send notifications for hostings expiring soon'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        expiring_hosting = Hosting.objects.filter(expiring_date__lte=today + timezone.timedelta(days=14), notified=False)

        for hosting in expiring_hosting:
            send_expiry_notification(hosting)
            hosting.notified = True
            hosting.save()
            self.stdout.write(self.style.SUCCESS(f"Notified {hosting.customer.email} about {hosting.domain_name}"))
