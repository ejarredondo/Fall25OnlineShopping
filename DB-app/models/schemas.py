from sqlalchemy import DateTime, CheckConstraint, Enum, ForeignKey, Date
from core import db
from sqlalchemy.sql import func


class Department(db.Model):
    __tablename__ = "department"

    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(20), nullable=False)
    employee_total = db.Column(db.Integer, nullable=False)

class Customer(db.Model):
    __tablename__ = "customer"

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))


class Employee(db.Model):
    __tablename__ = "employee"

    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    __tablename__ = "catalog"

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    sku = db.Column(db.Integer, unique=True, nullable=False)
    weight = db.Column(db.Numeric(5, 2))
    base_price = db.Column(db.Numeric(7, 2), CheckConstraint('base_price >= 0'), nullable=False)
    sale_price = db.Column(db.Numeric(7, 2), CheckConstraint('sale_price >= 0'), nullable=False)
    sold_by_weight_or_unit = db.Column(Enum('Weight', 'Unit'), nullable=False)
    brand = db.Column(db.String(255))
    quantity_of_item = db.Column(db.SmallInteger)
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'), nullable=False)
    expiration_date = db.Column(db.Date)

class Store(db.Model):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street_address = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip = db.Column(db.String(5), nullable=False)

class Supplier(db.Model):
    __tablename__ = "supplier"

    supplier_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    supplier_name = db.Column(db.String(255), unique=True, nullable=False)
    supplier_address_street = db.Column(db.String(255))
    supplier_address_city = db.Column(db.String(20))
    supplier_address_state = db.Column(db.String(2))
    supplier_address_zip = db.Column(db.String(5))
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id', ondelete='RESTRICT', onupdate='CASCADE'))

    store = db.relationship("Store", backref="suppliers")

class Transaction(db.Model):
    __tablename__ = "transaction"

    transaction_id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    cashier_employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id', ondelete='RESTRICT', onupdate='CASCADE'))
    incoming_or_outgoing = db.Column(Enum('I', 'O'))
    transaction_amount = db.Column(db.Numeric(5, 2), CheckConstraint('transaction_amount >= 0'), nullable=False)
    transaction_date = db.Column(db.DateTime)

class ItemSupplied(db.Model):
    __tablename__ = "item_supplied"

    product_id = db.Column(db.Integer, db.ForeignKey('catalog.product_id'), primary_key=True)
    transaction_id = db.Column(db.SmallInteger, db.ForeignKey('transaction.transaction_id'), primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'))
    item_quantity = db.Column(db.SmallInteger, nullable=False)

class DietaryInformation(db.Model):
    __tablename__ = "dietary_information"

    product_id = db.Column(db.Integer, db.ForeignKey('catalog.product_id'), primary_key=True)
    restriction = db.Column(
        Enum('DairyFree', 'GlutenFree', 'vegetarian', 'vegan', 'kosher', 'keto',
             'SugarFree', 'LowCarb', 'PorkFree', 'NutFree', 'ShellfishFree', 'SoyFree')
    )

class CustomerPurchaseHistory(db.Model):
    __tablename__ = "customer_purchase_history"

    customer_purchase_history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    transaction_id = db.Column(db.SmallInteger, db.ForeignKey('transaction.transaction_id'))
    amount_spent = db.Column(db.Numeric(5, 2))
    date_purchased = db.Column(db.Date)
    time_purchased = db.Column(db.Time)

class CustomerTransaction(db.Model):
    __tablename__ = "customer_transaction"

    customer_transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    transaction_id = db.Column(db.SmallInteger, db.ForeignKey('transaction.transaction_id'))
    shipping_address_street = db.Column(db.String(30))
    shipping_address_city = db.Column(db.String(30))
    shipping_address_state = db.Column(db.String(2))
    shipping_address_zip = db.Column(db.String(5))
    card_info = db.Column(db.String(30), unique=True)
    email_address = db.Column(db.String(30), unique=True)
    items_purchased = db.Column(db.SmallInteger)

class EmployeeTransaction(db.Model):
    __tablename__ = "employee_transaction"

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), primary_key=True)
    transaction_id = db.Column(db.SmallInteger, db.ForeignKey('transaction.transaction_id'), primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'))


# Aliases to match the helper modules' expected class names
Department = Department
department = Department
Customer = Customer
customer = Customer
Employee = Employee
employee = Employee
Catalog = Catalog
catalog = Catalog
Store = Store
store = Store
Supplier = Supplier
supplier = Supplier
Transaction = Transaction
transaction = Transaction






