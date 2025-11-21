
from sqlalchemy import func
from models.schemas import Department #change table names
from core import ma, db

def get_department(): 
    all_departments = Department.query.all()
    return department_schema.dump(all_departments)

def add_department(DepartmentName, EmployeeTotal):
    d = Department(DepartmentName=DepartmentName, EmployeeTotal=EmployeeTotal, last_update=func.now())
    db.session.add(d)
    db.session.commit()

def delete_department(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Department.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class departmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department

actor_schema = departmentSchema()
actors_schema = departmentSchema(many=True)

