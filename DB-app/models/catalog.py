
from sqlalchemy import func
from models.schemas import Catalog
from core import ma, db

def get_catalogs(): 
    all_catalogs = Catalog.query.all()
    return catalogs_schema.dump(all_catalogs)

def add_catalog(product_name, category, sku, weight, 
              base_price, sale_price, sold_by_weight_or_unit, 
              brand, quantity_of_item, department_id, expiration_date):
    a = Catalog(product_name = product_name, category = category, 
                sku = sku, weight = weight, base_price = base_price, 
                sale_price = sale_price, sold_by_weight_or_unit = sold_by_weight_or_unit, 
                brand = brand, quantity_of_item = quantity_of_item, department_id = department_id, 
                expiration_date = expiration_date, last_update=func.now())
    # need to add foreign key for department ID; consult reference on canvas
    db.session.add(a)
    db.session.commit()

def delete_catalog(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Catalog.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class CatalogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Catalog

catalog_schema = CatalogSchema()
catalogs_schema = CatalogSchema(many=True)
