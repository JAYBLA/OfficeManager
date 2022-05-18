from .models import Invoice

import timezone
from datetime import timedelta

base_url = settings.BASE_URL

def my_scheduled_job():
  invoices = Invoice.objects.filter(category=hosting, status=Unpaid)
  for invoice in invoices:
    if (invoice.send_date + timedelta(days=7)) >= timezone.now():
      email = invoice.customer.email
      customer = invoice.customer.name
      c=customer.upper()
      invoice_no = 'JB100R' + str(invoice.customer.id)+str(c[0]+str(c[1])+str(c[2]))
      due_date = invoice.due_date
      
      data = {
          'invoice':invoice,
          'invoice_no':invoice_no,
          'created_at':invoice.date,
          'due_date':due_date,
          'base_url':base_url,
      }
    
      pdf = render_to_pdf('invoice/pdf-templatejaybla.html', data)
      invoice.invoice_file.save(str(datetime.now())+'invoice.pdf', File(BytesIO(pdf.content)))
      mail = EmailMessage('JAYBLA GROUP', "Reminder Invoice", to=[email], from_email=settings.EMAIL_HOST_USER)
      mail.content_subtype = 'html'
      mail.attach('invoice.pdf', pdf.getvalue(), 'application/pdf')
      mail.send()
      invoice.send_date = timezone.now()
      invoice.save()
    else:
      pass
