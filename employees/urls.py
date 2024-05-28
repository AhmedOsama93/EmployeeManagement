from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from django.urls import path, include
import employees

app_name = employees
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
