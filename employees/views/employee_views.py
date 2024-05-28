'''
you can use ModelViewSet like this but i prefer generic views 
 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
