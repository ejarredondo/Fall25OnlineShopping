from models.schemas import CustomerPurchaseHistory, customer as Customer, Transaction
from core import ma, db


def get_customerpurchasehistory():
    records = CustomerPurchaseHistory.query.all()
    return customer_purchase_histories_schema.dump(records)


def get_purchase_history_by_customer(customer_id: int):
    records = (
        db.session.query(CustomerPurchaseHistory)
        .join(Customer, CustomerPurchaseHistory.customer_id == Customer.customer_id)
        .filter(Customer.customer_id == customer_id)
        .all()
    )
    return records


def get_purchase_history_by_transaction(transaction_id: int):
    records = (
        db.session.query(CustomerPurchaseHistory)
        .join(Transaction, CustomerPurchaseHistory.transaction_id == Transaction.transaction_id)
        .filter(Transaction.transaction_id == transaction_id)
        .all()
    )
    return records


def add_customerpurchasehistory(
    customer_id: int,
    transaction_id: int,
    amount_spent,
    date_purchased,
    time_purchased,
):
    record = CustomerPurchaseHistory(
        customer_id=customer_id,
        transaction_id=transaction_id,
        amount_spent=amount_spent,
        date_purchased=date_purchased,
        time_purchased=time_purchased,
    )
    db.session.add(record)
    db.session.commit()


def delete_customerpurchasehistory(history_id: int):
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
