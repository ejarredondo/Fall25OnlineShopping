
from models.schemas import Store
from core import ma, db


def get_stores():
    all_stores = Store.query.all()
    return stores_schema.dump(all_stores)


def get_store(store_id):
    return Store.query.get(store_id)


def add_store(street_address, city, state, zip_code, employee_number=None):
    a = Store(
        street_address=street_address,
        city=city,
        state=state,
        zip=zip_code,
        employee_number=employee_number,
    )
    db.session.add(a)
    db.session.commit()


def delete_store(store_id):
    store_to_delete = Store.query.get(store_id)
    if store_to_delete is None:
        return
    db.session.delete(store_to_delete)
    db.session.commit()


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store
        include_fk = True


store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)
