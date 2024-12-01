# Generated by Django 5.0.3 on 2024-04-24 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0008_patientfiles_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='active',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=10),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=6, null=True)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.appointment')),
            ],
        ),
    ]
