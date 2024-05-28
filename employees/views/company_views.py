
'''
you can use ModelViewSet like this but i prefer generic views 
 
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
'''


from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from employees.models import Company
from employees.serializers import CompanySerializer


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDestroyAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
