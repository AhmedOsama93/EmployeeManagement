from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)

    position = models.CharField(max_length=50)
    date_joined = models.DateField()
    country = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.email}"
