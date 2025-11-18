from sqlalchemy import ItemSupplied
from models.schemas import ItemSupllied
from core import ma, db

def get_ItemSupplied(): 
    all_ItemsSupplied = ItemSupplied.query.all()
    return ItemsSupplied_schema.dump(all_ItemsSupplied)

def get_ItemsSupplied(ID):
    ItemSupplied = ItemSupplied.query.get()
    return ItemSupplied

def add_ItemSupplied(Item_Quantity, SupplierID, TransactionID, Primary_ID, store_id):
    IS = ItemSupplied(Item_Quantity=Item_Quantity, SupplierID=SupplierID, TransactionID=TransactionID, 
                      Primary_ID=Primary_ID, store_id=store_id, last_update=func.now())
    db.session.add(IS)
    db.session.commit()

def delete_ItemSupplied(Product_ID, Transaction_ID):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = ItemSupplied.query.filter_by(Product_ID=Product_ID, Transaction_ID=Transaction_ID).first()
	db.session.delete(data)
	db.session.commit()
     
class ItemSuppliedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemSupplied

item_supplied_schema = ItemSuppliedSchema()
item_supplieds_schema = ItemSuppliedSchema(many=True)

