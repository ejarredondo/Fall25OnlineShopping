from models.schemas import DietaryInformation, catalog as Catalog
from core import ma, db


def get_DietaryInformation():
    return dietary_informations_schema.dump(DietaryInformation.query.all())


def get_all_DietaryInformation_by_Catalog(product_id):
    catalogs = (
        db.session.query(DietaryInformation)
        .join(Catalog, DietaryInformation.product_id == Catalog.product_id)
        .filter(Catalog.product_id == product_id)
        .all()
    )
    return catalogs


def add_DietaryInformation(product_id, restriction):
    di = DietaryInformation(product_id=product_id, restriction=restriction)
    db.session.add(di)
    db.session.commit()


def delete_DietaryInformation(product_id):
    data = DietaryInformation.query.get(product_id)
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class DietaryInformationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DietaryInformation
        include_fk = True


dietary_information_schema = DietaryInformationSchema()
dietary_informations_schema = DietaryInformationSchema(many=True)
