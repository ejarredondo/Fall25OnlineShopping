from core import app
from decimal import Decimal, InvalidOperation
from datetime import datetime
from flask import redirect, request, url_for 
from flask.templating import render_template
from models import catalog, customer, customerpurchasehistory, customertransaction, department, DietaryInformation, employee, employeetransaction, ItemSupllied, store, supplier, Transaction

# A decorator used to tell the application 
# which URL is associated with which function 
@app.route('/hello')	 
def hello(): 
	return 'HELLO'

# APP ROUTE TO RENDER HOME PAGE WITH LINKS
	# check this with home.html; might need to delete home.html??
@app.route('/')
def index():
	return render_template('index.html')

# APP ROUTE TO GET RESULTS FOR CATALOG SELECT QUERY 
@app.route('/get_catalogs', methods=['GET']) 
def get_results(): 
	catalogs = catalog.get_catalogs()
	return render_template('catalog.html', catalogs=catalogs) 

@app.route('/get_all_catalogs_by_dept/<int:id>', methods=['GET']) 
def get_all_catalogs_by_dept(department_id): 
	catalogs = catalog.get_all_catalogs_by_dept(department_id)
	departments = department.get_department(id)
	return render_template('catalogs_select.html', catalogs = catalogs , departments = departments)  

@app.route('/get_catalogs_without_dept/add_catalog_to_dept', methods=['POST']) 
def add_catalogs_without_dept(): 
	product_id = request.form.get("product_id")
	department_id = request.form.get("department_id")
	catalog.add_catalog_to_dept(product_id, department_id)
	return redirect (url_for('get_catalog_dept', id=department_id))  

# APP ROUTE TO RENDER FORM TO ADD CATALOG DATA
@app.route('/add_catalogs')
def add_catalogs():
	return render_template('add_catalog.html')

# APP ROUTE TO CALL FUNCTION TO ADD CATALOG
@app.route('/add', methods=["POST"])
def add_catalog():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	product_name = request.form.get("product_name")
	category = request.form.get("category")
	sku = request.form.get("sku")
	weight = request.form.get("weight")
	base_price = request.form.get("base_price")
	sale_price = request.form.get("sale_price")
	sold_by_weight_or_unit = request.form.get("sold_by_weight_or_unit")
	brand = request.form.get("brand")
	quantity_of_item = request.form.get("quantity_of_item")
	department_id = request.form.get("department_id")
	expiration_date = request.form.get("expiration_date")

	# call model function that will store data as a row in our datatable
	if product_name != '' and category != '' and sku != '' and base_price != '' and sale_price != '' and sold_by_weight_or_unit != '' and department_id != '':
		catalog.add_catalog(product_name, category, sku, 
					  weight, base_price, sale_price, sold_by_weight_or_unit,
					  brand, quantity_of_item, department_id, expiration_date)
		return redirect('/')
	else:
		return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE CATALOG
@app.route('/delete_catalog/<int:id>')
def delete_catalog(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	catalog.delete_catalog(id)
	return redirect('/')

# APP ROUTE TO GET RESULTS FOR SUPPLIER SELECT QUERY 
@app.route('/get_suppliers', methods=['GET']) 
def get_results(): 
	suppliers = supplier.get_suppliers()
	return render_template('supplier.html', suppliers = suppliers) 

@app.route('/get_all_suppliers_by_store/<int:id>', methods=['GET']) 
def get_all_suppliers_by_store(store_id): 
	suppliers = supplier.get_all_suppliers_by_store(store_id)
	store = store.get_store(id)
	return render_template('suppliers_select.html', suppliers = suppliers, store = store)  

@app.route('/get_suppliers_without_store/add_suppliers_to_store', methods=['POST']) 
def add_suppliers_without_store(): 
	supplier_id = request.form.get("supplier_id")
	store_id = request.form.get("store_id")
	supplier.add_supplier_to_store(supplier_id, store_id)
	return redirect (url_for('get_supplier_store', id=store_id))  

# APP ROUTE TO RENDER FORM TO ADD SUPPLIER DATA
@app.route('/add_suppliers')
def add_suppliers():
	return render_template('add_supplier.html')

# APP ROUTE TO CALL FUNCTION TO ADD SUPPLIER
@app.route('/add', methods=["POST"])
def add_supplier():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	supplier_name = request.form.get("supplier_name")
	supplier_address_street = request.form.get("supplier_address_street")
	supplier_address_city = request.form.get("supplier_address_city")
	supplier_address_state = request.form.get("supplier_address_state")
	supplier_address_zip = request.form.get("supplier_address_zip")
	store_id = request.form.get("store_id")

	# call model function that will store data as a row in our datatable
	if supplier_name != '':
		supplier.add_supplier(supplier_name, supplier_address_street, supplier_address_city, 
					  supplier_address_state, supplier_address_zip, store_id)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/delete_supplier/<int:id>')
def delete_supplier(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	supplier.delete_supplier(id)
	return redirect('/')

# APP ROUTE TO GET RESULTS FOR STORE SELECT QUERY 
@app.route('/get_stores', methods=['GET']) 
def get_results(): 
	stores = store.get_stores()
	return render_template('store.html', stores = stores) 

# APP ROUTE TO RENDER FORM TO ADD STORE DATA
@app.route('/add_stores')
def add_stores():
	return render_template('add_store.html')

# APP ROUTE TO CALL FUNCTION TO ADD STORE
@app.route('/add', methods=["POST"])
def add_store():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	street_address = request.form.get("street_address")
	city = request.form.get("city")
	state = request.form.get("state")
	zip = request.form.get("zip")

	# call model function that will store data as a row in our datatable
	if street_address!= '' and city != '' and state != '' and zip != '':
		supplier.add_supplier(street_address, city, state, zip)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/delete_store/<int:id>')
def delete_store(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	store.delete_store(id)
	return redirect('/')

# APP ROUTE TO GET RESULTS FOR DEPARTMENT QUERY 
@app.route('/get_department', methods=['GET','POST']) 
def get_department(): 
	department = department.get_department()
	return render_template('departments.html', department=department)  

# APP ROUTE TO CALL FUNCTION TO DELETE A department
@app.route('/delete_film/<int:id>')
def delete_department(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	department.delete_department(id)
	return redirect('/')

@app.route('/department/add', methods=['GET'])
def add_department_form():
	return render_template('add_department.html')


# APP ROUTE TO GET RESULTS FOR FILM QUERY 
@app.route('/get_films', methods=['GET','POST']) 
def get_films(): 
	films = Film.get_films()
	return render_template('films.html', films=films)  

# APP ROUTE TO GET RESULTS FOR FILM AND ACTORS QUERY 
@app.route('/get_film_actors/<int:id>', methods=['GET','POST']) 
def get_film_actors(id): 
	film = Film.get_film(id)
	film_actors = FilmActor.get_film_actors(id)
	return render_template('film_actor.html', film=film, film_actors=film_actors)  

# APP ROUTE TO ADD AN ACTOR TO A FILM 
#@app.route('/add_actor_to_film/<int:film_id>/<int:actor_id>', methods=['GET','POST']) 
#def add_actor_to_film(film_id,actor_id): 
#	FilmActor.add_actor_to_film(film_id,actor_id)
#	film = Film.get_films(id)
#	film_actors = FilmActor.get_film_actors(id)
#	return render_template('film_actor.html', film=film, film_actors=film_actors)  

# APP ROUTE TO CALL FUNCTION TO DELETE A FILM
@app.route('/delete_film/<int:id>')
def delete_film(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	Film.delete_film(id)
	return redirect('/')

# APP ROUTES FOR CUSTOMER TABLE
@app.route('/customers', methods=['GET'])
def get_customers():
	customers = customer.get_customers()
	return render_template('customer.html', customers=customers)


@app.route('/customers/add', methods=['GET'])
def add_customer_form():
	return render_template('add_customer.html')


@app.route('/customers', methods=['POST'])
def add_customer():
	first_name = (request.form.get("first_name") or "").strip()
	last_name = (request.form.get("last_name") or "").strip()

	if first_name and last_name:
		customer.add_customer(first_name, last_name)

	return redirect(url_for('get_customers'))


@app.route('/customers/<int:customer_id>/delete', methods=['GET'])
def delete_customer(customer_id):
	customer.delete_customer(customer_id)
	return redirect(url_for('get_customers'))

# APP ROUTES FOR EMPLOYEE TABLE
@app.route('/employees', methods=['GET'])
def get_employees():
	employees = employee.get_employees()
	return render_template('employee.html', employees=employees)


@app.route('/employees/add', methods=['GET'])
def add_employee_form():
	return render_template('add_employee.html')


@app.route('/employees', methods=['POST'])
def create_employee():
	first_name = (request.form.get("first_name") or "").strip()
	last_name = (request.form.get("last_name") or "").strip()
	start_date_raw = (request.form.get("start_date") or "").strip()
	pay_rate_raw = (request.form.get("pay_rate") or "").strip()
	position = (request.form.get("position") or "").strip() or None
	availability_raw = request.form.get("availability", "").strip().lower()
	bank_routing_information = (request.form.get("bank_routing_information") or "").strip()
	checking_account_number = (request.form.get("checking_account_number") or "").strip()
	email_address = (request.form.get("email_address") or "").strip() or None

	start_date = None
	if start_date_raw:
		try:
			start_date = datetime.strptime(start_date_raw, "%Y-%m-%d").date()
		except ValueError:
			start_date = None

	pay_rate = None
	if pay_rate_raw:
		try:
			pay_rate = Decimal(pay_rate_raw)
		except InvalidOperation:
			pay_rate = None

	availability = None
	if availability_raw in ("true", "false"):
		availability = availability_raw == "true"

	if (
		first_name
		and last_name
		and pay_rate is not None
		and bank_routing_information
		and checking_account_number
	):
		employee.add_employee(
			first_name,
			last_name,
			start_date,
			pay_rate,
			position,
			availability,
			bank_routing_information,
			checking_account_number,
			email_address,
		)

	return redirect(url_for('get_employees'))


@app.route('/employees/<int:employee_id>/delete', methods=['GET'])
def delete_employee(employee_id):
	employee.delete_employee(employee_id)
	return redirect(url_for('get_employees'))

@app.route('/get_DietaryInformation', methods=['GET']) 
def get_results(): 
	DietaryInformation = DietaryInformation.get_DietaryInformation()
	return render_template('DietaryInformation.html', DietaryInformations=DietaryInformation) 

@app.route('/get_all_DietaryInformation_by_dept/<int:id>', methods=['GET']) 
def get_all_DietaryInformation_by_Catalog(Product_id): 
	DietaryInformation = DietaryInformation.get_all_DietaryInformation_by_Catalog(Product_id)
	catalogs = catalog.get_catalog(Product_id)
	return render_template('catalogs_select.html', catalogs = catalogs , DietaryInformations = DietaryInformation)  

@app.route('/get_DietaryInformation_without_Catalog/add_DietaryInformation_to_Catalog', methods=['POST']) 
def add_DietaryInformation_without_Catalog(): 
	product_id = request.form.get("product_id")
	catalog.add_catalog_to_dept(product_id)
	return redirect (url_for('get_DietaryInformation_Catalog', id=product_id))  

# APP ROUTE TO RENDER FORM TO ADD CATALOG DATA
@app.route('/add_DietaryInformations')
def add_DietaryInformations():
	return render_template('add_DietaryInformation.html')

# APP ROUTE TO CALL FUNCTION TO ADD CATALOG
@app.route('/add', methods=["POST"])
def add_catalog():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	product_ID = request.form.get("product_ID")
	Restriction = request.form.get("Restriction")
	

	# call model function that will store data as a row in our datatable
	if product_ID != '' and Restriction != '':
		DietaryInformation.add_DietaryInformation(product_ID, Restriction)
		return redirect('/')
	else:
		return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE CATALOG
@app.route('/delete_DietaryInformation/<int:Product_id>')
def delete_DietaryInformation(Product_id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	DietaryInformation.delete_DietaryInformation(Product_id)
	return redirect('/')


@app.route('/get_Transaction', methods=['GET']) 
def get_results(): 
	transactions = Transaction.get_Transaction()
	return render_template('transaction.html', transactions=transactions) 

@app.route('/get_all_Transaction_by_Employee/<int:id>', methods=['GET']) 
def get_all_Transaction_by_Employee(CashierEmployee_id): 
	transactions = Transaction.get_all_Transaction_by_Employee(CashierEmployee_id)
	return render_template('transactions_select.html', transactions=transactions, Employee=employee)  

@app.route('/get_transaction_without_Employee/add_Transaction_to_Employee', methods=['POST']) 
def add_Transaction_without_Employee(): 
	Transaction_id = request.form.get("Transaction_id")
	CashierEmployee_id = request.form.get("CashierEmployee_id")
	Transaction.add_Transaction_to_Employee(Transaction_id, CashierEmployee_id)
	return redirect (url_for('get_all_Transaction_by_Employee', id=CashierEmployee_id))  

# APP ROUTE TO RENDER FORM TO ADD CATALOG DATA
@app.route('/add_Transaction')
def add_Transaction():
	return render_template('add_Transaction.html')

# APP ROUTE TO CALL FUNCTION TO ADD CATALOG
@app.route('/add', methods=["POST"])
def add_Transaction():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	Transaction_ID = request.form.get("Transaction_ID")
	CashierEmployee_id = request.form.get("CashierEmployee_id")
	IncomingOrOutgoing = request.form.get("IncomingOrOutgoing")
	Transaction_amount = request.form.get("Transaction_amount")
	Transaction_Date = request.form.get("Transaction_Date")
	
	# call model function that will store data as a row in our datatable
	if Transaction_ID != '' and CashierEmployee_id != '' and IncomingOrOutgoing != '' and Transaction_amount != '' and Transaction_Date != '':
		Transaction.add_Transaction(Transaction_ID, CashierEmployee_id, IncomingOrOutgoing, Transaction_amount, Transaction_Date)
		return redirect('/')
	else:
		return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE CATALOG
@app.route('/delete_Transaction/<int:id>')
def delete_Transaction(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	Transaction.delete_Transaction(id)
	return redirect('/')


@app.route('/get_ItemSupplied', methods=['GET']) 
def get_results(): 
	ItemSupplied = ItemSupplied.get_ItemSupplied()
	return render_template('ItemSupplied.html', ItemSupplied=ItemSupplied) 

@app.route('/get_all_ItemsSupplied_by_catalog/<int:id>', methods=['GET']) 
def get_all_ItemsSupplied_by_catalog(Product_id): 
	ItemSupplied = ItemSupplied.get_all_ItemsSupplied_by_catalog(Product_id)
	return render_template('ItemSupplied_select.html', ItemSupplied=ItemSupplied, catalog=catalog) 

def get_all_ItemsSupplied_by_Transaction(Transaction_id): 
	ItemSupplied = ItemSupplied.get_all_ItemsSupplied_by_Transaction(Transaction_id)
	return render_template('ItemSupplied_select.html', ItemSupplied=ItemSupplied, Transaction=Transaction) 

def get_all_ItemsSupplied_by_Supplier(Supplier_id): 
	ItemSupplied = ItemSupplied.get_all_ItemsSupplied_by_Supplier(Supplier_id)
	return render_template('ItemSupplied_select.html', ItemSupplied=ItemSupplied, Supplier=supplier)

def get_all_ItemsSupplied_by_Store(Store_id): 
	ItemSupplied = ItemSupplied.get_all_ItemsSupplied_by_Store(Store_id)
	return render_template('ItemSupplied_select.html', ItemSupplied=ItemSupplied, Store=store)

@app.route('/get_ItemSupplied_without_catalog/add_ItemSupplied_to_catalog', methods=['POST']) 
def add_ItemSupplied_without_catalog(): 
	product_id = request.form.get("product_id")
	catalog_id = request.form.get("catalog_id")
	ItemSupplied.add_ItemSupplied_to_catalog(product_id, catalog_id)
	return redirect (url_for('get_ItemSupplied_catalog', id=catalog_id))  

# APP ROUTE TO RENDER FORM TO ADD CATALOG DATA
@app.route('/add_ItemSupplied')
def add_ItemSupplied():
	return render_template('add_ItemSupplied.html')

# APP ROUTE TO CALL FUNCTION TO ADD CATALOG
@app.route('/add', methods=["POST"])
def add_ItemSupplied():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	ProductID = request.form.get("ProductID")
	TransactionID = request.form.get("TransactionID")
	SupplierID = request.form.get("SupplierID")
	ItemQuantity = request.form.get("ItemQuantity")


	# call model function that will store data as a row in our datatable
	if ProductID != '' and TransactionID != '' and SupplierID != '' and ItemQuantity != '':
		ItemSupplied.add_ItemSupplied(ProductID, TransactionID, SupplierID, ItemQuantity)
		return redirect('/')
	else:
		return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE CATALOG
@app.route('/delete_ItemSupplied/<int:id>')
def delete_ItemSupplied(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	ItemSupplied.delete_ItemSupplied(id)
	return redirect('/')

# APP ROUTE TO GET RESULTS FOR FILM QUERY 
@app.route('/get_queries', methods=['GET']) 
def get_queries(): 
	return render_template('queries.html')  

# APP ROUTE TO GET TOP 5 CUSTOMERS QUERY 
@app.route('/get_top5custs', methods=['GET']) 
def get_top5custs(): 
	top5custs = Queries.get_top5custs()
	return render_template('top5custs.html', top5custs=top5custs) 

# APP ROUTE TO GET AVERAGE RENTAL QUERY 
@app.route('/get_avg_rental', methods=['GET']) 
def get_avg_rental(): 
	avg_rental = Queries.get_avg_rental()
	return render_template('avg_rental.html', avg_rental=avg_rental) 

if __name__=='__main__': 
    app.run(port=8001, debug=True) 
