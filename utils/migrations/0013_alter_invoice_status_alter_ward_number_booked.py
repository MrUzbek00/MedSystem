# Generated by Django 5.0.3 on 2024-04-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0012_department_doctors_alter_invoice_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(blank=True, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ward',
            name='number_booked',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
