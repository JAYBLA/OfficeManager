# Generated by Django 3.2.5 on 2021-07-22 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_invoice_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]