from sqlalchemy import DateTime, CheckConstraint, Enum, ForeignKey, Date
from core import db
from sqlalchemy.sql import func

# Models
class Actor(db.Model):

    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    
class Film(db.Model):

    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    release_year = db.Column(db.Integer, nullable=True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    
class FilmActor(db.Model):

    actor_id = db.Column(db.Integer, db.ForeignKey('actor.actor_id'), primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.film_id'), primary_key=True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())









class Department(db.Model):

    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(20), nullable=False)
    employee_total = db.Column(db.Integer, nullable=False)


class Customer(db.Model):

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))


class Employee(db.Model):

    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date)
    pay_rate = db.Column(db.Numeric(8, 2), nullable=False)
    position = db.Column(db.String(50))
    availability = db.Column(db.Boolean)
    bank_routing_information = db.Column(db.String(9), nullable=False)
    checking_account_number = db.Column(db.String(17), nullable=False)
    email_address = db.Column(db.String(250))


class Catalog(db.Model):

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    sku = db.Column(db.Integer, unique=True, nullable=False)
    weight = db.Column(db.Numeric(5, 2))
    base_price = db.Column(db.Numeric(7, 2), CheckConstraint('base_price >= 0'), nullable=False)
    sale_price = db.Column(db.Numeric(7, 2), CheckConstraint('sale_price >= 0'), nullable=False)
    sold_by_weight_or_unit = db.Column(db.Enum('Weight', 'Unit'), nullable=False)
    brand = db.Column(db.String(255))
    quantity_of_item = db.Column(db.SmallInteger)
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'), nullable=False)
    expiration_date = db.Column(db.Date)


class Store(db.Model):

    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street_address = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip = db.Column(db.String(5), nullable=False)

class Supplier(db.Model):

    supplier_name = db.Column(db.String(255), unique=True, nullable=False)
    supplier_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    supplier_address_street = db.Column(db.String(255))
    supplier_address_city = db.Column(db.String(20))
    supplier_address_state = db.Column(db.String(2))
    supplier_address_zip = db.Column(db.String(5))
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id', ondelete='RESTRICT', onupdate='CASCADE'))
















