from models.schemas import CustomerPurchaseHistory, Customer, Transac
from sqlalchemy import func
from core import ma, db

def get_customer_purchase_history():
    records = CustomerPurchaseHistory.query.all()
    return customer_purchase_histories_schema.dump(records)

def get_customer_purchase_history_by_id(history_id: int):
    record = CustomerPurchaseHistory.query.get(history_id)
    return record

def get_purchase_history_by_customer(customer_id: int):
    records = (
        db.session.query(CustomerPurchaseHistory)
        .join(Customer, CustomerPurchaseHistory.CustomerID == Customer.CustomerID)
        .filter(Customer.CustomerID == customer_id)
        .all()
    )
    return records

def get_purchase_history_by_transaction(transaction_id: int):
    records = (
        db.session.query(CustomerPurchaseHistory)
        .join(Transac, CustomerPurchaseHistory.TransactionID == Transac.TransactionID)
        .filter(Transac.TransactionID == transaction_id)
        .all()
    )
    return records

def add_customer_purchase_history(
    CustomerID: int,
    TransactionID: int,
    AmountSpent,
    DatePurchased,
    TimePurchased,
):
    record = CustomerPurchaseHistory(
        CustomerID=CustomerID,
        TransactionID=TransactionID,
        AmountSpent=AmountSpent,
        DatePurchased=DatePurchased,
        TimePurchased=TimePurchased,
    )

    db.session.add(record)
    db.session.commit()

def delete_customer_purchase_history(history_id: int):
    record = CustomerPurchaseHistory.query.get(history_id)

    if record is None:
        return

    db.session.delete(record)
    db.session.commit()

class CustomerPurchaseHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerPurchaseHistory


customer_purchase_history_schema = CustomerPurchaseHistorySchema()
customer_purchase_histories_schema = CustomerPurchaseHistorySchema(many=True)
