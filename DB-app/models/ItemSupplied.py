from models.schemas import ItemSupplied, catalog as Catalog, Transaction, Supplier, Store
from core import ma, db


def get_ItemSupplied():
    all_items = ItemSupplied.query.all()
    return item_supplied_schema.dump(all_items)


def get_all_ItemSupplied_by_Catalog(ProductID):
    items = (
        db.session.query(ItemSupplied)
        .join(Catalog, ItemSupplied.product_id == Catalog.ProductID)
        .filter(Catalog.ProductID == ProductID)
        .all()
    )
    return items


def get_all_ItemSupplied_by_Transaction(TransactionID):
    items = (
        db.session.query(ItemSupplied)
        .join(Transaction, ItemSupplied.transaction_id == Transaction.TransactionID)
        .filter(Transaction.TransactionID == TransactionID)
        .all()
    )
    return items


def get_all_ItemSupplied_by_supplier(SupplierID):
    items = (
        db.session.query(ItemSupplied)
        .join(Supplier, ItemSupplied.supplier_id == Supplier.SupplierID)
        .filter(Supplier.SupplierID == SupplierID)
        .all()
    )
    return items


def get_all_ItemSupplied_by_Store(StoreID):
    items = (
        db.session.query(ItemSupplied)
        .join(Store, ItemSupplied.store_id == Store.StoreID)
        .filter(Store.StoreID == StoreID)
        .all()
    )
    return items


def get_ItemSupplied_without_Catalog():
    return db.session.query(ItemSupplied).filter(ItemSupplied.ProductID.is_(None)).all()


def get_ItemSupplied_without_Transaction():
    return db.session.query(ItemSupplied).filter(ItemSupplied.TransactionID.is_(None)).all()


def get_ItemSupplied_without_Supplier():
    return db.session.query(ItemSupplied).filter(ItemSupplied.SupplierID.is_(None)).all()


def get_ItemSupplied_without_Store():
    return db.session.query(ItemSupplied).filter(ItemSupplied.StoreID.is_(None)).all()


def add_ItemSupplied(ProductID, TransactionID, SupplierID, StoreID, ItemQuantity):
    is_record = ItemSupplied(
        ProductID=ProductID,
        TransactionID=TransactionID,
        SupplierID=SupplierID,
        StoreID=StoreID,
        ItemQuantity=ItemQuantity,
    )
    db.session.add(is_record)
    db.session.commit()


def delete_ItemSupplied(ProductID, TransactionID):
    data = ItemSupplied.query.filter_by(ProductID=ProductID, TransactionID=TransactionID).first()
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class ItemSuppliedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemSupplied


item_supplied_schema = ItemSuppliedSchema()
item_supplieds_schema = ItemSuppliedSchema(many=True)
