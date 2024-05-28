'''
you can use ModelViewSet like this but i prefer generic views 
 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''

from rest_framework import viewsets, mixins

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
