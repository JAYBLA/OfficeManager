from django.template.loader import render_to_string
from weasyprint import HTML
from io import BytesIO
from django.core.mail import EmailMessage
from django.utils import timezone

def hosting_expire_email(hosting):
    customer_name = getattr(hosting.customer, 'name', 'Valued Customer')
    customer_email = getattr(hosting.customer, 'email', None)
    domain = getattr(hosting, 'domain', 'your domain')
    expiring_date = getattr(hosting, 'expiring_date', None)

    if not customer_email:
        print(f"Skipping email: No email found for {customer_name}")
        return

    subject = f"Hosting Expiry Notice for {domain}"
    message = (
        f"Dear {customer_name},\n\n"
        f"Your hosting for {domain} will expire on {expiring_date}. "
        f"Please find the attached invoice for renewal.\n\nThank you."
    )

    # Render invoice HTML to PDF
    html_string = render_to_string('hosting/invoice.html', {
        'hosting': hosting,
        'today': timezone.now().date()
    })

    pdf_file = BytesIO()
    HTML(string=html_string).write_pdf(target=pdf_file)
    pdf_file.seek(0)

    print("Tupoooo")

    try:
        email = EmailMessage(
            subject,
            message,
            'management@jayblagroup.co.tz',
            [customer_email],
        )

        email.attach(f"invoice_{hosting.id}.pdf", pdf_file.read(), 'application/pdf')
        email.send()
        print(f"Email sent to {customer_email} with dynamic invoice")
    except Exception as e:
        print(f"Error sending email: {e}")
