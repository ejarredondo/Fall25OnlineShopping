
from models.schemas import Store
from core import ma, db


def get_stores():
    all_stores = Store.query.all()
    return stores_schema.dump(all_stores)


def get_store(StoreID):
    return Store.query.get(StoreID)


def add_store(StreetAddress, City, State, Zip, EmployeeNumber=None):
    a = Store(
        StreetAddress=StreetAddress,
        City=City,
        State=State,
        Zip=Zip,
        EmployeeNumber=EmployeeNumber
    )
    db.session.add(a)
    db.session.commit()


def delete_store(StoreID):
    store_to_delete = Store.query.get(StoreID)
    if store_to_delete is None:
        return
    db.session.delete(store_to_delete)
    db.session.commit()


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store


store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)
