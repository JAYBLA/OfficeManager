# Generated by Django 3.2.5 on 2021-07-12 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0011_invoice_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='due_date',
        ),
    ]