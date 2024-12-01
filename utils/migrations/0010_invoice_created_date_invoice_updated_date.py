# Generated by Django 5.0.3 on 2024-04-24 10:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0009_appointment_active_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
