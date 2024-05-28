import phonenumbers
from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'position', 'date_joined', 'phone', 'country')

    def get_country(self):
        if phone := self.initial_data.get('phone'):
            parsed_phone = phonenumbers.parse(phone, None)
            country_code = phonenumbers.region_code_for_number(parsed_phone)

            if country_code == 'IL':
                country_code = "PS"
            return country_code
        raise serializers.ValidationError("Wrong phone number.")
