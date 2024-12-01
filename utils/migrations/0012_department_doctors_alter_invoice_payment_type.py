# Generated by Django 5.0.3 on 2024-04-24 13:01

import utils.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0011_invoice_payment_type_alter_appointment_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='doctors',
            field=models.ManyToManyField(blank=True, related_name='department_doctors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('card', 'Card'), ('cash', 'Cash')], max_length=10, null=utils.models.Invoice.Type),
        ),
    ]