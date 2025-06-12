from django_cron import CronJobBase, Schedule
from django.utils import timezone
from hosting.models import Hosting
from notifications.utils import send_expiry_notification
import datetime

class HostingExpiryNotificationCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'hosting.hosting_expiry_notification'  # unique code

    def do(self):
        with open('/home/jayblaco/logs/officemanager/expiry_cron.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} - Cron executed\n")
        today = timezone.now().date()
        upcoming = today + timezone.timedelta(days=14)
        expiring_hosting = Hosting.objects.filter(expiring_date__lte=upcoming, notified=False)

        for hosting in expiring_hosting:
            send_expiry_notification(hosting)
            hosting.notified = True
            hosting.save()
