
from sqlalchemy import func
from models.schemas import Department #change table names
from core import ma, db

def get_department(): 
    all_departments = departments.query.all()
    return actors_schema.dump(all_actors)

def add_department(DepartmentName, EmployeeTotal):
    d = Department(DepartmentName=DepartmentName, EmployeeTotal=EmployeeTotal, last_update=func.now())
    db.session.add(d)
    db.session.commit()

def delete_department(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = department.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class ActorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Actor

actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)

