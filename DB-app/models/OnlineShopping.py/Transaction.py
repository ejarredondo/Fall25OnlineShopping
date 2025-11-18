from sqlalchemy import Transaction
from models.schemas import ItemSupllied
from core import ma, db

def get_Transaction(): 
    all_Transaction = Transaction.query.all()
    return Transaction_schema.dump(all_Transaction)

def get_Transaction(ID):
    Transaction = Transaction.query.get(ID)
    return Transaction

def get_all_Transaction_by_Employee(Emplyee_id):
     Transaction = db.session.query(Transaction
            ).join(Employee, Transactiom.Employee_id == Employee.Employee_id
            ).filter(Employee.Employee_id == Employee_id
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

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)