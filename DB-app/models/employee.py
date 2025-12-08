from decimal import Decimal
from typing import Optional
from datetime import date
from models.schemas import Employee
from core import ma, db


def get_employees():
    employees = Employee.query.all()
    return employees_schema.dump(employees)


def add_employee(
    first_name: str,
    last_name: str,
    start_date: Optional[date],
    pay_rate: Decimal,
    position: Optional[str],
    availability: Optional[bool],
    bank_routing_information: str,
    checking_account_number: str,
    email_address: Optional[str],
):
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        start_date=start_date,
        pay_rate=pay_rate,
        position=position,
        availability=availability,
        bank_routing_information=bank_routing_information,
        checking_account_number=checking_account_number,
        email_address=email_address,
    )
    db.session.add(employee)
    db.session.commit()


def delete_employee(employee_id: int):
    employee = Employee.query.get(employee_id)
    if employee is None:
        return
    db.session.delete(employee)
    db.session.commit()


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_fk = True


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
