
from sqlalchemy import func
from models.schemas import catalog
from core import ma, db

def get_catalogs(): 
    all_catalogs = catalog.query.all()
    return catalogs_schema.dump(all_catalogs)

def add_catalog(productname, category, SKU, weight, 
              baseprice, saleprice, soldbyweightorunit, 
              brand, quantityofitem, departmentid, expirationdate):
    a = catalog(productname=productname, category = category, 
                SKU = SKU, weight = weight, baseprice = baseprice, saleprice = saleprice, 
                soldbyweightorunit = soldbyweightorunit, brand = brand, quantityofitem = quantityofitem, 
                departmentid = departmentid, expirationdate = expirationdate, last_update=func.now())
    # need to add foreign key for department ID; consult reference on canvas
    db.session.add(a)
    db.session.commit()

def delete_catalog(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = catalog.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class CatalogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = catalog

catalog_schema = CatalogSchema()
catalogs_schema = CatalogSchema(many=True)
