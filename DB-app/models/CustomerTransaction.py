from models.schemas import CustomerTransaction
from core import ma, db


def get_customer_transactions():
    transactions = CustomerTransaction.query.all()
    return customer_transactions_schema.dump(transactions)


def add_customer_transaction(
    CustomerID,
    TransactionID,
    ShippingAddressStreet=None,
    ShippingAddressCity=None,
    ShippingAddressState=None,
    ShippingAddressZip=None,
    CardInfo=None,
    EmailAddress=None,
    ItemsPurchased=None,
):
    transaction = CustomerTransaction(
        CustomerID=CustomerID,
        TransactionID=TransactionID,
        ShippingAddressStreet=ShippingAddressStreet,
        ShippingAddressCity=ShippingAddressCity,
        ShippingAddressState=ShippingAddressState,
        ShippingAddressZip=ShippingAddressZip,
        CardInfo=CardInfo,
        EmailAddress=EmailAddress,
        ItemsPurchased=ItemsPurchased,
    )
    db.session.add(transaction)
    db.session.commit()


def delete_customer_transaction(customer_transaction_id):
    transaction = CustomerTransaction.query.get(customer_transaction_id)
    if transaction is None:
        return
    db.session.delete(transaction)
    db.session.commit()


class CustomerTransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CustomerTransaction


customer_transaction_schema = CustomerTransactionSchema()
customer_transactions_schema = CustomerTransactionSchema(many=True)
