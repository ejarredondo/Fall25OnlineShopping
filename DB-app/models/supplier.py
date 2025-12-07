from models.schemas import Supplier, Store
from core import ma, db


def get_suppliers():
    all_suppliers = Supplier.query.all()
    return suppliers_schema.dump(all_suppliers)


def get_supplier(SupplierID):
    return Supplier.query.get(SupplierID)


def get_all_suppliers_by_store(StoreID):
    suppliers = (
        db.session.query(Supplier)
        .join(Store, Supplier.StoreID == Store.StoreID)
        .filter(Store.StoreID == StoreID)
        .all()
    )
    return suppliers


def get_suppliers_without_store():
    suppliers = db.session.query(Supplier).filter(Supplier.StoreID.is_(None)).all()
    return suppliers


def add_supplier_to_store(SupplierID, StoreID):
    supplier = Supplier.query.get(SupplierID)
    if supplier is None:
        return
    supplier.StoreID = StoreID
    db.session.commit()


def add_supplier(
    SupplierName,
    SupplierAddressStreet,
    SupplierAddressCity,
    SupplierAddressState,
    SupplierAddressZip,
    StoreID,
):
    a = Supplier(
        SupplierName=SupplierName,
        SupplierAddressStreet=SupplierAddressStreet,
        SupplierAddressCity=SupplierAddressCity,
        SupplierAddressState=SupplierAddressState,
        SupplierAddressZip=SupplierAddressZip,
        StoreID=StoreID,
    )

    db.session.add(a)
    db.session.commit()


def delete_supplier(SupplierID):
    supplier = Supplier.query.get(SupplierID)
    if supplier is None:
        return
    db.session.delete(supplier)
    db.session.commit()


class SupplierSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier


supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)
