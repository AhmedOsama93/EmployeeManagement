'''
you can use ModelViewSet like this but i prefer generic views 
 
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
'''

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from employees.models import Department
from employees.serializers import DepartmentSerializer


class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreateAPIView(CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveAPIView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentUpdateAPIView(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDestroyAPIView(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
