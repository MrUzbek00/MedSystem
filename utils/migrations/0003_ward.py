# Generated by Django 5.0.3 on 2024-04-20 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(default=0)),
                ('number_patients', models.IntegerField(default=1)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.department')),
            ],
        ),
    ]
