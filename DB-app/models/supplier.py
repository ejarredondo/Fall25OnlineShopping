from sqlalchemy import func
from models.schemas import Supplier
from core import ma, db

def get_suppliers(): 
    all_suppliers = Supplier.query.all()
    return suppliers_schema.dump(all_suppliers)

def get_supplier(id):
    supplier = Supplier.query.get(id)
    return supplier

def add_supplier(supplier_name, supplier_address_street, supplier_address_city, 
                 supplier_address_state, supplier_address_zip, store_id):
    a = Supplier(supplier_name = supplier_name, supplier_address_street = supplier_address_street, 
                 supplier_address_city = supplier_address_city, 
                 supplier_address_state = supplier_address_state, supplier_address_zip = supplier_address_zip, 
                 store_id = store_id, last_update=func.now())
    # add foreign key for store_id
    db.session.add(a)
    db.session.commit()

def delete_supplier(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Supplier.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class SupplierSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier

supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)

