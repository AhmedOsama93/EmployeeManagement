from employees.views.company_views import CompanyListAPIView, CompanyCreateAPIView, CompanyRetrieveAPIView, \
    CompanyUpdateAPIView, CompanyDestroyAPIView

from employees.views.department_views import DepartmentListAPIView, DepartmentCreateAPIView, DepartmentRetrieveAPIView, \
    DepartmentUpdateAPIView, DepartmentDestroyAPIView

from employees.views.employee_views import EmployeeListAPIView, EmployeeCreateAPIView, EmployeeRetrieveAPIView, \
    EmployeeUpdateAPIView, EmployeeDestroyAPIView

__all__ = (
    "CompanyListAPIView",
    "CompanyCreateAPIView",
    "CompanyRetrieveAPIView",
    "CompanyUpdateAPIView",
    "CompanyDestroyAPIView",

    "EmployeeListAPIView",
    "EmployeeCreateAPIView",
    "EmployeeRetrieveAPIView",
    "EmployeeUpdateAPIView",
    "EmployeeDestroyAPIView",

    "DepartmentListAPIView",
    "DepartmentCreateAPIView",
    "DepartmentRetrieveAPIView",
    "DepartmentUpdateAPIView",
    "DepartmentDestroyAPIView",
)
