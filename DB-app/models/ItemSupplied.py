from models.schemas import ItemSupplied, catalog as Catalog, Transaction, Supplier as Supplier, store as Store
from core import ma, db


def get_ItemSupplied():
    all_items = ItemSupplied.query.all()
    return item_supplieds_schema.dump(all_items)


def get_all_ItemSupplied_by_catalog(product_id):
    items = (
        db.session.query(ItemSupplied)
        .join(Catalog, ItemSupplied.product_id == Catalog.product_id)
        .filter(Catalog.product_id == product_id)
        .all()
    )
    return items


def get_all_ItemSupplied_by_Transaction(transaction_id):
    items = (
        db.session.query(ItemSupplied)
        .join(Transaction, ItemSupplied.transaction_id == Transaction.transaction_id)
        .filter(Transaction.transaction_id == transaction_id)
        .all()
    )
    return items


def get_all_ItemSupplied_by_supplier(supplier_id):
    items = (
        db.session.query(ItemSupplied)
        .join(Supplier, ItemSupplied.supplier_id == Supplier.supplier_id)
        .filter(Supplier.supplier_id == supplier_id)
        .all()
    )
    return items


def get_all_ItemSupplied_by_Store(store_id):
    items = (
        db.session.query(ItemSupplied)
        .join(Store, ItemSupplied.store_id == Store.store_id)
        .filter(Store.store_id == store_id)
        .all()
    )
    return items


def get_ItemSupplied_without_Catalog():
    return db.session.query(ItemSupplied).filter(ItemSupplied.product_id.is_(None)).all()


def get_ItemSupplied_without_Transaction():
    return db.session.query(ItemSupplied).filter(ItemSupplied.transaction_id.is_(None)).all()


def get_ItemSupplied_without_Supplier():
    return db.session.query(ItemSupplied).filter(ItemSupplied.supplier_id.is_(None)).all()


def get_ItemSupplied_without_Store():
    return db.session.query(ItemSupplied).filter(ItemSupplied.store_id.is_(None)).all()


def add_ItemSupplied(product_id, transaction_id, supplier_id, store_id, item_quantity):
    is_record = ItemSupplied(
        product_id=product_id,
        transaction_id=transaction_id,
        supplier_id=supplier_id,
        store_id=store_id,
        item_quantity=item_quantity,
    )
    db.session.add(is_record)
    db.session.commit()


def delete_ItemSupplied(product_id, transaction_id):
    data = ItemSupplied.query.filter_by(product_id=product_id, transaction_id=transaction_id).first()
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class ItemSuppliedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemSupplied


item_supplied_schema = ItemSuppliedSchema()
item_supplieds_schema = ItemSuppliedSchema(many=True)
