from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    email_validator = EmailValidator()

    name = models.CharField(max_length=100)

    phone = PhoneNumberField(
        blank=True,
        null=True,
        default=None,
    )

    phone = PhoneNumberField(
        blank=True,
        null=True,
        default=None,
        error_messages={'unique': _("A user with that phone already exists.")})

    email = models.EmailField(_('email address'),
                              validators=[email_validator],
                              unique=True, blank=False, null=True)
    logo = models.ImageField(upload_to='employees_logos/', null=True, blank=True)
    bio = models.CharField(_("Bio"), max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    join_date = models.DateField()
    image = models.ImageField(upload_to='employee_image/', null=True, blank=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.email}"
