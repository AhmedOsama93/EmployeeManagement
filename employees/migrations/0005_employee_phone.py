# Generated by Django 3.2.18 on 2024-05-28 10:28

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, error_messages={'unique': 'A user with that phone already exists.'}, max_length=128, null=True, region=None),
        ),
    ]