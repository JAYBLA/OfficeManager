from django_cron import CronJobBase, Schedule
from django.utils import timezone
from hosting.models import Hosting
from .utils import hosting_expire_email
import datetime


class HostingExpiryNotificationCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # For development

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'HostingExpiryNotificationCronJob'

    def do(self):        
        today = timezone.now().date()
        expiry_cutoff = today + timezone.timedelta(days=14)

        expiring_hostings = Hosting.objects.filter(
            expiring_date__gte=today,          # today or later
            expiring_date__lte=expiry_cutoff   # up to 14 days ahead
        )        
        for hosting in expiring_hostings:            
            # Only notify if not already notified today
            if not hosting.last_notified or hosting.last_notified != today:                
                hosting_expire_email(hosting)                
                hosting.last_notified = today
                hosting.save()

