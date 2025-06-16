from django_cron import CronJobBase, Schedule
from django.utils import timezone
from hosting.models import Hosting
<<<<<<< HEAD
from .utils import hosting_expire_email

=======
from notifications.utils import send_expiry_notification
import datetime
>>>>>>> 96731768ad1b5a6252077ae7ebd0506b12548f78

class HostingExpiryNotificationCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # For development

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'HostingExpiryNotificationCronJob'

    def do(self):
        with open('/home/jayblaco/logs/officemanager/expiry_cron.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} - Cron executed\n")
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

