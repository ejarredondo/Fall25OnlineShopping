from sqlalchemy import func
from models.schemas import Transaction, Employee
from core import ma, db


def get_Transaction(ID):
    Transaction = Transaction.query.get(ID)
    return Transaction

def get_all_Transaction_by_Employee(CashierEmployee_id):
     Transaction = db.session.query(Transaction
            ).join(Employee, Transaction.CashierEmployee_id == Employee.Employee_id
            ).filter(Employee.Employee_id == CashierEmployee_id
            ).all()

     return Transaction

def get_Transaction_without_Employee():
    Transaction = db.session.query(Transaction).filter(
         Transaction.Employee_id.is_(None)
    ).all()

    return Transaction


def add_Transaction(CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate):
    T = Transaction(CashierEmployeeID=CashierEmployeeID, IncomingOrOutgoing=IncomingOrOutgoing, TransactionAmount=TransactionAmount, TransactionDate=TransactionDate, last_update=func.now())
    db.session.add(T)
    db.session.commit()

def delete_Transaction(Transaction_ID):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Transaction.query.get(Transaction_ID)
	db.session.delete(data)
	db.session.commit()

class TransacSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction

transaction_schema = TransacSchema()
transactions_schema = TransacSchema(many=True)