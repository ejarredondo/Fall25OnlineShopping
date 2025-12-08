
from sqlalchemy import func  # noqa: F401
from models.schemas import catalog as Catalog, department as Department
from core import ma, db


def get_catalogs():
    catalogs = Catalog.query.all()
    return catalogs_schema.dump(catalogs)


def get_catalog(product_id):
    return Catalog.query.get(product_id)


def get_all_catalogs_by_dept(department_id):
    catalogs = (
        db.session.query(Catalog)
        .join(Department, Catalog.department_id == Department.department_id)
        .filter(Department.department_id == department_id)
        .all()
    )
    return catalogs


def get_catalogs_without_dept():
    catalogs = db.session.query(Catalog).filter(Catalog.department_id.is_(None)).all()
    return catalogs


def add_catalog_to_dept(product_id, department_id):
    catalog_item = Catalog.query.get(product_id)
    if catalog_item is None:
        return
    catalog_item.department_id = department_id
    db.session.commit()


def add_catalog(
    product_name,
    category,
    sku,
    weight,
    base_price,
    sale_price,
    sold_by_weight_or_unit,
    brand,
    quantity_of_item,
    department_id,
    expiration_date,
):
    a = Catalog(
        product_name=product_name,
        category=category,
        sku=sku,
        weight=weight,
        base_price=base_price,
        sale_price=sale_price,
        sold_by_weight_or_unit=sold_by_weight_or_unit,
        brand=brand,
        quantity_of_item=quantity_of_item,
        department_id=department_id,
        expiration_date=expiration_date,
    )

    db.session.add(a)
    db.session.commit()


def delete_catalog(product_id):
    data = Catalog.query.get(product_id)
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class CatalogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Catalog
        include_fk = True


catalog_schema = CatalogSchema()
catalogs_schema = CatalogSchema(many=True)
