# Generated by Django 3.2.5 on 2021-07-12 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0003_auto_20210705_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
