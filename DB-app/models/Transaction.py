from sqlalchemy import func
from models.schemas import Transac, Employee
from core import ma, db


def get_Transaction(ID):
    Transaction = Transac.query.get(ID)
    return Transac

def get_all_Transaction_by_Employee(CashierEmployee_id):
     Transac = db.session.query(Transac
            ).join(Employee, Transac.CashierEmployee_id == Employee.Employee_id
            ).filter(Employee.Employee_id == CashierEmployee_id
            ).all()

     return Transaction

def get_Transaction_without_Employee():
    Transac = db.session.query(Transac).filter(
         Transac.Employee_id.is_(None)
    ).all()

    return Transac


def add_Transac(CashierEmployeeID, IncomingOrOutgoing, TransactionAmount, TransactionDate):
    T = Transac(CashierEmployeeID=CashierEmployeeID, IncomingOrOutgoing=IncomingOrOutgoing, TransactionAmount=TransactionAmount, TransactionDate=TransactionDate, last_update=func.now())
    db.session.add(T)
    db.session.commit()

def delete_Transac(Transac_ID):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Transac.query.get(Transac_ID)
	db.session.delete(data)
	db.session.commit()

class TransacSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transac

transaction_schema = TransacSchema()
transactions_schema = TransacSchema(many=True)