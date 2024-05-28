from django.urls import path

from employees.views import CompanyListAPIView, CompanyCreateAPIView, CompanyRetrieveAPIView, CompanyUpdateAPIView, \
    CompanyDestroyAPIView, EmployeeListAPIView, EmployeeCreateAPIView, EmployeeRetrieveAPIView, EmployeeUpdateAPIView, \
    EmployeeDestroyAPIView, DepartmentListAPIView, DepartmentCreateAPIView, DepartmentRetrieveAPIView, \
    DepartmentUpdateAPIView, DepartmentDestroyAPIView

app_name = 'employees'

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view(), name='company-list'),
    path('companies/create/', CompanyCreateAPIView.as_view(), name='company-create'),
    path('companies/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='company-retrieve'),
    path('companies/<int:pk>/update/', CompanyUpdateAPIView.as_view(), name='company-update'),
    path('companies/<int:pk>/delete/', CompanyDestroyAPIView.as_view(), name='company-delete'),

    path('employees/', EmployeeListAPIView.as_view(), name='Employee-list'),
    path('employees/create/', EmployeeCreateAPIView.as_view(), name='Employee-create'),
    path('employees/<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='Employee-retrieve'),
    path('employees/<int:pk>/update/', EmployeeUpdateAPIView.as_view(), name='Employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDestroyAPIView.as_view(), name='Employee-delete'),

    path('departments/', DepartmentListAPIView.as_view(), name='Department-list'),
    path('departments/create/', DepartmentCreateAPIView.as_view(), name='Department-create'),
    path('departments/<int:pk>/', DepartmentRetrieveAPIView.as_view(), name='Department-retrieve'),
    path('departments/<int:pk>/update/', DepartmentUpdateAPIView.as_view(), name='Department-update'),
    path('departments/<int:pk>/delete/', DepartmentDestroyAPIView.as_view(), name='Department-delete'),
]