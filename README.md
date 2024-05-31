#O verview
The Employee Management System is designed to streamline the management of companies, departments, and employees. It provides a comprehensive solution for creating, reading, updating, and deleting (CRUD) records for these entities. The system includes a workflow for handling the onboarding process of new employees and implements role-based access control to ensure secure data handling.


## Features

CRUD operations for companies, departments, and employees.
Workflow for employee onboarding.
Role-based access control.
RESTful API for all models.
User-friendly interface for managing entities.
Optional features include unit and integration testing, logging, and summary dashboards.

## Back End

### Models
1. **User Accounts**
   - User Name
   - Email Address (Login ID)
   - Role

2. **Company**
   - Company Name
   - Number of Departments
   - Number of Employees

3. **Department**
   - Company (Select)
   - Department Name
   - Number of Employees

4. **Employee**
   - Company (Select)
   - Department (Select - only related to selected company)
   - Employee Status (handled through a workflow)
   - Employee Name
   - Email Address
   - Mobile Number
   - Address
   - Designation (Position/Title)
   - Hired On (only if hired)
   - Days Employed (only if hired)


```
    pip install -r requirements.txt
    
    cd EmployeeManagement
    
    python manage.py migrate
    
    python manage.py runserver
```
