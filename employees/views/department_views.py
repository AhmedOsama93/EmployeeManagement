'''
you can use ModelViewSet like this but i prefer generic views 
 
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
'''

from rest_framework import viewsets, mixins
from employees.models import Department
from employees.serializers import DepartmentSerializer


class DepartmentListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDestroyViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
