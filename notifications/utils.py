from django.core.mail import send_mail

def send_expiry_notification(hosting):
    subject = f"Hosting Expiry Notice for {hosting.domain_name}"
    message = f"Dear {hosting.customer.username},\n\nYour hosting for {hosting.domain_name} will expire on {hosting.expiry_date}. Please renew it in time."
    send_mail(
        subject,
        message,
        'management@jayblagroup.co.tz',  # from email
        [hosting.customer.email],
        fail_silently=False,
    )
