from sqlalchemy import DateTime, CheckConstraint, Enum, ForeignKey, Date
from core import db
from sqlalchemy.sql import func

class department(db.Model):

    DepartmentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DepartmentName = db.Column(db.String(20), nullable=False)
    EmployeeTotal = db.Column(db.Integer, nullable=False)


class customer(db.Model):

    CustomerID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    FirstName = db.Column(db.String(30))
    LastName = db.Column(db.String(30))


class employee(db.Model):

    EmployeeID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    FirstName = db.Column(db.String(100), nullable=False)
    LastName = db.Column(db.String(100), nullable=False)
    StartDate = db.Column(db.Date)
    PayRate = db.Column(db.Numeric(8, 2), nullable=False)
    Position = db.Column(db.String(50))
    Availability = db.Column(db.Boolean)
    BankRoutingInformation = db.Column(db.String(9), nullable=False)
    CheckingAccountNumber = db.Column(db.String(17), nullable=False)
    EmailAddress = db.Column(db.String(250))


class catalog(db.Model):

    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    ProductName = db.Column(db.String(255), nullable=False)
    Category = db.Column(db.String(255), nullable=False)
    SKU = db.Column(db.Integer, unique=True, nullable=False)
    Weight = db.Column(db.Numeric(5, 2))
    BasePrice = db.Column(db.Numeric(7, 2), CheckConstraint('BasePrice >= 0'), nullable=False)
    SalePrice = db.Column(db.Numeric(7, 2), CheckConstraint('SalePrice >= 0'), nullable=False)
    SoldByWeightOrUnit = db.Column(db.Enum('Weight', 'Unit'), nullable=False)
    Brand = db.Column(db.String(255))
    QuantityOfItem = db.Column(db.SmallInteger)
    DepartmentID = db.Column(db.Integer, db.ForeignKey('department.department_id'), nullable=False)
    ExpirationDate = db.Column(db.Date)


class Store(db.Model):
    __tablename__ = "Store"
    StoreID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    StreetAddress = db.Column(db.String(30), nullable=False)
    City = db.Column(db.String(30), nullable=False)
    State = db.Column(db.String(2), nullable=False)
    Zip = db.Column(db.String(5), nullable=False)
    EmployeeNumber = db.Column(db.Integer, nullable=True)

class Supplier(db.Model):
    __tablename__ = "Supplier"
    SupplierName = db.Column(db.String(255), unique=True, nullable=False)
    SupplierID = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    SupplierAddressStreet = db.Column(db.String(255))
    SupplierAddressCity = db.Column(db.String(20))
    SupplierAddressState = db.Column(db.String(2))
    SupplierAddressZip = db.Column(db.String(5))
    StoreID = db.Column(db.Integer, db.ForeignKey('Store.StoreID', ondelete='RESTRICT', onupdate='CASCADE'))
    store = db.relationship("Store", backref="suppliers")

class Transaction(db.Model):

    __tablename__ = 'Transaction'

    TransactionID = db.Column(db.SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    CashierEmployeeID = db.Column(db.Integer, db.ForeignKey('employee.EmployeeID', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    IncomingOrOutgoing = db.Column(db.Enum('I', 'O'))
    TransactionAmount = db.Column(db.Numeric(5, 2), CheckConstraint('TransactionAmount >= 0'), nullable=False)
    TransactionDate = db.Column(db.DateTime)

class ItemSupplied(db.Model):

    ProductID = db.Column(db.Integer, db.ForeignKey('catalog.product_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    TransactionID = db.Column(db.SmallInteger, db.ForeignKey('transaction.TransactionID', ondelete='RESTRICT', onupdate='CASCADE'),  primary_key=True, nullable=False)
    SupplierID = db.Column(db.Integer, db.ForeignKey('supplier.SupplierID', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    StoreID = db.Column(db.Integer, db.ForeignKey('store.StoreID', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    ItemQuantity = db.Column(db.SmallInteger, nullable=False)

class DietaryInformation(db.Model):

    ProductID = db.Column(db.Integer, db.ForeignKey('catalog.product_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    Restriction = db.Column(db.Enum('DairyFree', 'GlutenFree', 'vegetarian', 'vegan', 'kosher', 'keto', 'SugarFree', 'LowCarb', 'PorkFree', 'NutFree', 'ShellfishFree', 'SoyFree'))

class CustomerPurchaseHistory(db.Model):

    CustomerPurchaseHistoryID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('customer.customer_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    TransactionID = db.Column(db.SmallInteger, db.ForeignKey('transaction.TransactionID', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    AmountSpent = db.Column(db.Numeric(5, 2), nullable=False)
    DatePurchased = db.Column(db.Date)
    TimePurchased = db.Column(db.Time)

class CustomerTransaction(db.Model):

    CustomerTransactionID = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('customer.customer_id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    TransactionID = db.Column(db.SmallInteger, db.ForeignKey('transaction.TransactionID', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    ShippingAddressStreet = db.Column(db.String(30))
    ShippingAddressCity = db.Column(db.String(30))
    ShippingAddressState = db.Column(db.String(2))
    ShippingAddressZip = db.Column(db.String(5))
    CardInfo = db.Column(db.String(30), unique=True)
    EmailAddress = db.Column(db.String(30), unique=True)
    ItemsPurchased = db.Column(db.SmallInteger)

class EmployeeTransaction(db.Model):

    EmployeeID = db.Column(db.Integer, db.ForeignKey('employee.employee_id', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    TransactionID = db.Column(db.SmallInteger, db.ForeignKey('transaction.TransactionID', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    StoreID = db.Column(db.Integer, db.ForeignKey('store.StoreID', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)


# Aliases to match the helper modules' expected class names
Department = department
Customer = customer
Employee = employee
Catalog = catalog
Store = Store
Supplier = Supplier
Transaction = Transaction







