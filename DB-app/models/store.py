
from sqlalchemy import func
from models.schemas import Store
from core import ma, db

def get_stores(): 
    all_stores = Store.query.all()
    return stores_schema.dump(all_stores)

def get_store(id):
    store = Store.query.get(id)
    return store

def add_store(StreetAddress, City, State, Zip):
    a = Store(StreetAddress = StreetAddress, City = City, State = State, Zip = Zip, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_store(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Store.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

