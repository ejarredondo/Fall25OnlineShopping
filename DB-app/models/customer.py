from models.schemas import Customer
from core import ma, db


def get_customers():
    customers = Customer.query.all()
    return customers_schema.dump(customers)


def add_customer(first_name, last_name):
    customer = Customer(first_name=first_name, last_name=last_name)
    db.session.add(customer)
    db.session.commit()


def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return
    db.session.delete(customer)
    db.session.commit()


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
