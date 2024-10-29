from datetime import date
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema
from typing import List

from crud.models import Employee

api = NinjaAPI()


class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None

class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: int | None = None
    birthdate: date | None = None

class EmployeeUp(Schema):
    first_name: str | None = None
    last_name: str | None = None
    department_id: int | None = None
    birthdate: date | None = None


@api.get('/hello')
def hello(request, name: str | None = None) -> str:
    if name:
        return f'Pozdrawiam wszystich Polaków. I Ciebie {name}, Pielgrzymie'
    return 'Sieg Heil'

@api.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

@api.get("/employees/", response=List[EmployeeOut])
def get_employees(request):
    employees = Employee.objects.all()
    return employees


@api.post("/employee")
def create_employee(request, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}


@api.put("/employees/{employee_id}")
def update_employee(request, employee_id: int, payload: EmployeeUp):
    employee = get_object_or_404(Employee, id=employee_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}


@api.delete("/employees/{employee_id}")
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True}
