from models.schemas import Transaction, employee as Employee
from core import ma, db


def get_Transaction(id):
    return Transaction.query.get(id)


def get_transactions():
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


def add_Transaction(TransactionID, CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate):
    t = Transaction(
        TransactionID=TransactionID,
        CashierEmployeeID=CashierEmployeeID,
        IncomingOrOutgoing=IncomingOrOutgoing,
        TransactionAmount=TransactionAmount,
        TransactionDate=TransactionDate,
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


transaction_schema = TransacSchema()
transactions_schema = TransacSchema(many=True)
