from sqlalchemy import func
from models.schemas import ItemSupplied, Catalog, Transaction, Supplier, Store
from core import ma, db

def get_ItemSupplied(): 
    all_ItemSupplied = ItemSupplied.query.all()
    return ItemSuppliedSchema.dump(all_ItemSupplied)



def get_all_ItemSupplied_by_catalog(Product_ID):
    ItemSupplied = db.session.query(ItemSupplied
            ).join(Catalog, ItemSupplied.Catalog_productID == Catalog.Product_ID
            ).filter(Catalog.Product_ID == Product_ID
            ).all()
    return ItemSupplied

def get_all_ItemSupplied_by_Transaction(Transaction_ID):
    ItemSupplied = db.session.query(ItemSupplied
            ).join(Transaction, ItemSupplied.TransactionID == Transaction.TransactionID
            ).filter(Transaction.TransactionID == Transaction_ID
            ).all()
    return ItemSupplied

def get_all_ItemSupplied_by_supplier(Supplier_ID):
    ItemSupplied = db.session.query(ItemSupplied
            ).join(Supplier, ItemSupplied.SupplierID == Supplier.SupplierID
            ).filter(Supplier.SupplierID == Supplier_ID
            ).all()
    return ItemSupplied

def get_all_ItemSupplied_by_Store(Store_ID):
    ItemSupplied = db.session.query(ItemSupplied
            ).join(Store, ItemSupplied.Store_ID == Store.Store_ID
            ).filter(Store.Store_ID == Store_ID
            ).all()
    return ItemSupplied

def get_ItemSupplied_without_Catalog():
    ItemSupplied = db.session.query(ItemSupplied).filter(
          ItemSupplied.Catalog_productID.is_(None)
    ).all()
    return ItemSupplied

def get_ItemSupplied_without_Transaction():
    ItemSupplied = db.session.query(ItemSupplied).filter(
          ItemSupplied.Transaction_ID.is_(None)
    ).all()
    return ItemSupplied

def get_ItemSupplied_without_Supplier():
    ItemSupplied = db.session.query(ItemSupplied).filter(
          ItemSupplied.Supplier_ID.is_(None)
    ).all()
    return ItemSupplied

def get_ItemSupplied_without_Store():
    ItemSupplied = db.session.query(ItemSupplied).filter(
          ItemSupplied.Store_ID.is_(None)
    ).all()
    return ItemSupplied

def add_ItemSupplied(Item_Quantity, SupplierID, TransactionID, Product_ID, Store_ID):
    IS = ItemSupplied(Item_Quantity=Item_Quantity, SupplierID=SupplierID, TransactionID=TransactionID, 
                      Product_ID=Product_ID, Store_ID=Store_ID, last_update=func.now())
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

