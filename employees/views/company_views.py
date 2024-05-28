
'''
you can use ModelViewSet like this but i prefer generic views 
 
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
'''

from rest_framework import viewsets, mixins
from employees.models import Company
from employees.serializers import CompanySerializer


class CompanyListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet
                         ):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet
                           ):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet
                             ):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDestroyViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
