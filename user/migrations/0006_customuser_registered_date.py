# Generated by Django 5.0.3 on 2024-04-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_customuser_specialization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='registered_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]