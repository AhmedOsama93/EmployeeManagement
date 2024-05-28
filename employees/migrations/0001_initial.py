# Generated by Django 3.2.18 on 2024-05-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(max_length=50)),
                ('date_joined', models.DateField()),
                ('country', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
