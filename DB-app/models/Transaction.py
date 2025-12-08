from models.schemas import Transaction, employee as Employee
from core import ma, db

def get_Transaction(transaction_id):
    return Transaction.query.get(transaction_id)


def get_Transactions():
    return Transaction.query.all()


def get_all_Transaction_by_Employee(cashier_employee_id):
    transactions = (
        db.session.query(Transaction)
        .join(Employee, Transaction.cashier_employee_id == Employee.employee_id)
        .filter(Employee.employee_id == cashier_employee_id)
        .all()
    )
    return transactions


def get_Transaction_without_Employee():
    transactions = db.session.query(Transaction).filter(Transaction.cashier_employee_id.is_(None)).all()
    return transactions


def add_Transaction(cashier_employee_id, incoming_or_outgoing, transaction_amount, transaction_date):
    t = Transaction(
        cashier_employee_id=cashier_employee_id,
        incoming_or_outgoing=incoming_or_outgoing,
        transaction_amount=transaction_amount,
        transaction_date=transaction_date,
    )
    db.session.add(t)
    db.session.commit()


def delete_Transaction(TransactionID):
    data = Transaction.query.get(TransactionID)
    if data is None:
        return
    db.session.delete(data)
    db.session.commit()


class TransacSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        include_fk = True


transaction_schema = TransacSchema()
transactions_schema = TransacSchema(many=True)
