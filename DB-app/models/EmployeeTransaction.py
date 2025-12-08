from models.schemas import EmployeeTransaction
from core import ma, db


def get_employee_transactions():
    records = EmployeeTransaction.query.all()
    return employee_transactions_schema.dump(records)


def add_employee_transaction(employee_id, transaction_id, store_id):
    record = EmployeeTransaction(
        employee_id=employee_id,
        transaction_id=transaction_id,
        store_id=store_id,
    )
    db.session.add(record)
    db.session.commit()


def delete_employee_transaction(employee_id, transaction_id):
    record = EmployeeTransaction.query.get((employee_id, transaction_id))
    if record is None:
        return
    db.session.delete(record)
    db.session.commit()


class EmployeeTransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeTransaction
        include_fk = True


employee_transaction_schema = EmployeeTransactionSchema()
employee_transactions_schema = EmployeeTransactionSchema(many=True)
