import phonenumbers
from rest_framework import serializers
from .models import Company, Department, Employee
from django.utils.translation import gettext as _


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'phone', 'email', 'logo', 'bio', 'created_at', 'updated_at')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'company')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id', 'first_name', 'last_name', 'email', 'phone', 'department', 'age', 'join_date', 'image', 'country')

    def validate_country(self, value):

        if phone := self.initial_data.get('phone'):
            parsed_phone = phonenumbers.parse(phone, None)
            country_code = phonenumbers.region_code_for_number(parsed_phone)

            if country_code == 'IL':
                country_code = "PS"
            if country_code == value:
                return value
        raise serializers.ValidationError(_("Wrong country type."))
