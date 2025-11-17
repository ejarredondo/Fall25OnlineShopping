
from sqlalchemy import func
from models.schemas import Catalog, Department 
from core import ma, db

def get_catalogs(product_id): 
    catalog_item = db.session.query(Catalog
                ).join(Department, Catalog.department_id == Department.department_id
                ).filter(Catalog.product_id == product_id
                ).first()
    
    return catalog_item

def get_all_catalogs_by_dept(department_id):
    catalogs = db.session.query(Catalog
            ).join(Department, Catalog.department_id == Department.department_id
            ).filter(Department.department_id == department_id
            ).all()
     
    return catalogs

def get_catalogs_without_dept():
    catalogs = db.session.query(Catalog).filter(
          Catalog.department_id.is_(None)
    ).all()
    
    return catalogs

def add_catalog(product_name, category, sku, weight, 
              base_price, sale_price, sold_by_weight_or_unit, 
              brand, quantity_of_item, department_id, expiration_date):
    
    a = Catalog(product_name = product_name, category = category, 
                sku = sku, weight = weight, base_price = base_price, 
                sale_price = sale_price, sold_by_weight_or_unit = sold_by_weight_or_unit, 
                brand = brand, quantity_of_item = quantity_of_item, department_id = department_id, 
                expiration_date = expiration_date, last_update=func.now())

    db.session.add(a)
    db.session.commit()

def delete_catalog(product_id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Catalog.query.get(product_id)
	db.session.delete(data)
	db.session.commit()
     
class CatalogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Catalog

catalog_schema = CatalogSchema()
catalogs_schema = CatalogSchema(many=True)
