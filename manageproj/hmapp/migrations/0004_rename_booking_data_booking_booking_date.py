# Generated by Django 4.2.7 on 2024-05-14 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmapp', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_data',
            new_name='booking_date',
        ),
    ]
