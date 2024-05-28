from employees.views.company_views import CompanyListViewSet, CompanyCreateViewSet, CompanyRetrieveViewSet, \
    CompanyUpdateViewSet, CompanyDestroyViewSet

from employees.views.department_views import DepartmentListViewSet, DepartmentCreateViewSet, DepartmentRetrieveViewSet, \
    DepartmentUpdateViewSet, DepartmentDestroyViewSet

from employees.views.employee_views import EmployeeListViewSet, EmployeeCreateViewSet, EmployeeRetrieveViewSet, \
    EmployeeUpdateViewSet, EmployeeDestroyViewSet

__all__ = (
    "CompanyListViewSet",
    "CompanyCreateViewSet",
    "CompanyRetrieveViewSet",
    "CompanyUpdateViewSet",
    "CompanyDestroyViewSet",

    "EmployeeListViewSet",
    "EmployeeCreateViewSet",
    "EmployeeRetrieveViewSet",
    "EmployeeUpdateViewSet",
    "EmployeeDestroyViewSet",

    "DepartmentListViewSet",
    "DepartmentCreateViewSet",
    "DepartmentRetrieveViewSet",
    "DepartmentUpdateViewSet",
    "DepartmentDestroyViewSet",
)
