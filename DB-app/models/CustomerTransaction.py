from models.schemas import CustomerTransaction
from core import ma, db


def get_customer_transactions():
    transactions = CustomerTransaction.query.all()
    return customer_transactions_schema.dump(transactions)


def add_customer_transaction(
    customer_id,
    transaction_id,
    shipping_address_street=None,
    shipping_address_city=None,
    shipping_address_state=None,
    shipping_address_zip=None,
    card_info=None,
    email_address=None,
    items_purchased=None,
):
    transaction = CustomerTransaction(
        customer_id=customer_id,
        transaction_id=transaction_id,
        shipping_address_street=shipping_address_street,
        shipping_address_city=shipping_address_city,
        shipping_address_state=shipping_address_state,
        shipping_address_zip=shipping_address_zip,
        card_info=card_info,
        email_address=email_address,
        items_purchased=items_purchased,
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
        include_fk = True


customer_transaction_schema = CustomerTransactionSchema()
customer_transactions_schema = CustomerTransactionSchema(many=True)
