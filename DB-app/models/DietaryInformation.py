from sqlalchemy import func
from models.schemas import DietaryInformation, Catalog
from core import ma, db

def get_DietaryInformation(): 
    all_DietaryInformation = DietaryInformation.query.all()
    return DietaryInformation_schema.dump(all_DietaryInformation)

def get_DietaryInformation(product_id): 
    DietaryInformation_item = db.session.query(DietaryInformation
                ).join(Catalog, DietaryInformation.ProductId == Catalog.Product_ID
                ).filter(DietaryInformation.ProductId == product_id
                ).first()

    return DietaryInformation_item

def get_all_DietaryInformation_by_Catalog(Product_id):
    catalogs = db.session.query(DietaryInformation
            ).join(Catalog, DietaryInformation.ProductId == Catalog.Product_ID
            ).filter(Catalog.Product_ID == Product_id
            ).all()
     
    return catalogs

def add_DietaryInformation(ProductId, Restriction):
    DI = DietaryInformation(ProductId=ProductId, Restriction=Restriction, last_update=func.now())
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