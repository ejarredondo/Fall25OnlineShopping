from models.schemas import supplier as Supplier, store as Store
from core import ma, db


def get_suppliers():
    all_suppliers = Supplier.query.all()
    return suppliers_schema.dump(all_suppliers)


def get_supplier(id):
    return Supplier.query.get(id)


def get_all_suppliers_by_store(store_id):
    suppliers = (
        db.session.query(Supplier)
        .join(Store, Supplier.store_id == Store.store_id)
        .filter(Store.store_id == store_id)
        .all()
    )
    return suppliers


def get_suppliers_without_store():
    suppliers = db.session.query(Supplier).filter(Supplier.store_id.is_(None)).all()
    return suppliers


def add_supplier_to_store(supplier_id, store_id):
    supplier = Supplier.query.get(supplier_id)
    if supplier is None:
        return
    supplier.store_id = store_id
    db.session.commit()


def add_supplier(
    supplier_name,
    supplier_address_street,
    supplier_address_city,
    supplier_address_state,
    supplier_address_zip,
    store_id,
):
    a = Supplier(
        supplier_name=supplier_name,
        supplier_address_street=supplier_address_street,
        supplier_address_city=supplier_address_city,
        supplier_address_state=supplier_address_state,
        supplier_address_zip=supplier_address_zip,
        store_id=store_id,
    )

    db.session.add(a)
    db.session.commit()


def delete_supplier(id):
    data = Supplier.query.get(id)
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class SupplierSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier


supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)
