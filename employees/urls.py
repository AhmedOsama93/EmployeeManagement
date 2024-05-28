from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeListViewSet,
    EmployeeCreateViewSet,
    EmployeeRetrieveViewSet,
    EmployeeUpdateViewSet,
    EmployeeDestroyViewSet
)

app_name = 'employees'
router = DefaultRouter()

router.register(r'employees-list', EmployeeListViewSet, basename='employees-list')
router.register(r'employees-create', EmployeeCreateViewSet, basename='employees-create')
router.register(r'employees-retrieve', EmployeeRetrieveViewSet, basename='employees-retrieve')
router.register(r'employees-update', EmployeeUpdateViewSet, basename='employees-update')
router.register(r'employees-destroy', EmployeeDestroyViewSet, basename='employees-destroy')

urlpatterns = router.urls
