from models.schemas import EmployeeTransaction
from core import ma, db


def get_employee_transactions():
    records = EmployeeTransaction.query.all()
    return employee_transactions_schema.dump(records)


def add_employee_transaction(EmployeeID, TransactionID, StoreID):
    record = EmployeeTransaction(
        EmployeeID=EmployeeID,
        TransactionID=TransactionID,
        StoreID=StoreID,
    )
    db.session.add(record)
    db.session.commit()


def delete_employee_transaction(EmployeeID, TransactionID):
    record = EmployeeTransaction.query.get((EmployeeID, TransactionID))
    if record is None:
        return
    db.session.delete(record)
    db.session.commit()


class EmployeeTransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeTransaction


employee_transaction_schema = EmployeeTransactionSchema()
employee_transactions_schema = EmployeeTransactionSchema(many=True)
