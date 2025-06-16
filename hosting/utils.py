from django.template.loader import render_to_string
from io import BytesIO
from django.core.mail import EmailMessage
from django.utils import timezone

# Import xhtml2pdf's pisa module
from xhtml2pdf import pisa

def hosting_expire_email(hosting):
    customer_name = hosting.customer.name
    customer_email = hosting.customer.email
    domain_name = hosting.domain
    expiring_date = hosting.expiring_date
    subject = f"Hosting Expiry Notice for {domain_name}"
    message = (
        f"Dear {customer_name},\n\n"
        f"Your hosting for {domain_name} will expire on {expiring_date}. "
        f"Please find the attached invoice for renewal.\n\nThank you."
    )

    # Render invoice HTML
    html_string = render_to_string('hosting/invoice.html', {
        'hosting': hosting,
        'today': timezone.now().date()
    })

    pdf_file = BytesIO()
    # Convert HTML to PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(src=html_string, dest=pdf_file)

    if pisa_status.err:
        print("Error generating PDF")
        return  # Or handle the error appropriately

    pdf_file.seek(0)

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
