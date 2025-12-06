
from models.schemas import store as Store
from core import ma, db


def get_stores():
    all_stores = Store.query.all()
    return stores_schema.dump(all_stores)


def get_store(id):
    return Store.query.get(id)


def add_store(street_address, city, state, zip_code):
    a = Store(
        street_address=street_address,
        city=city,
        state=state,
        zip=zip_code,
    )
    db.session.add(a)
    db.session.commit()


def delete_store(id):
    data = Store.query.get(id)
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store


store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)
