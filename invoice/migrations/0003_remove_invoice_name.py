# Generated by Django 3.1.7 on 2021-03-22 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_invoice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='name',
        ),
    ]