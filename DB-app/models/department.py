
from models.schemas import department as Department
from core import ma, db


def get_department(id=None):
    if id is None:
        all_departments = Department.query.all()
        return departments_schema.dump(all_departments)
    return Department.query.get(id)


def add_department(department_name, employee_total):
    d = Department(
        department_name=department_name,
        employee_total=employee_total,
    )
    db.session.add(d)
    db.session.commit()


def delete_department(id):
    data = Department.query.get(id)
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department
        include_fk = True


department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)
