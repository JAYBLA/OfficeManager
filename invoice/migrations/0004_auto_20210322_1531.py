# Generated by Django 3.1.7 on 2021-03-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_remove_invoice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='cost',
            field=models.IntegerField(),
        ),
    ]