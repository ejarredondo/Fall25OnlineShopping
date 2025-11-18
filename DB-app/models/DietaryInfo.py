from sqlalchemy import DietaryInformation
from models.schemas import DietaryInformation
from core import ma, db

def get_DietaryInformation(): 
    all_DietaryInformation = DietaryInformation.query.all()
    return DietaryInformation_schema.dump(all_DietaryInformation)

def add_DietaryInformation(Restriction):
    DI = DietaryInformation(Restriction=Restriction, last_update=func.now())
    db.session.add(DI)
    db.session.commit()

def delete_DietaryInformation(Product_ID):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = DietaryInformation.query.get(Product_ID)
	db.session.delete(data)
	db.session.commit()

class DietaryInformationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DietaryInformation

dietary_information_schema = DietaryInformationSchema()
dietary_informations_schema = DietaryInformationSchema(many=True)