from sqlalchemy import func
from models.schemas import Transac, Employee
from core import ma, db

def get_Transac(): 
    all_Transaction = Transaction.query.all()
    return Transaction_schema.dump(all_Transaction)

def get_Transac(ID):
    Transaction = Transaction.query.get(ID)
    return Transaction

def get_all_Transac_by_Employee(CashierEmployee_id):
     Transac = db.session.query(Transac
            ).join(Employee, Transac.CashierEmployee_id == Employee.Employee_id
            ).filter(Employee.Employee_id == CashierEmployee_id
            ).all()

     return Transac

def get_Transac_without_Employee():
    Transac = db.session.query(Transac).filter(
         Transac.Employee_id.is_(None)
    ).all()

    return Transac


def add_Transac(CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate):
    T = Transaction(CashierEmployeeID=CashierEmployeeID, IncomingOrOutgoing=IncomingOrOutgoing, TransactionAmount=TransactionAmount, TransactionDate=TransactionDate, last_update=func.now())
    db.session.add(T)
    db.session.commit()

def delete_Transaction(Transaction_ID):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Transac.query.get(Transaction_ID)
	db.session.delete(data)
	db.session.commit()

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)