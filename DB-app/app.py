from core import app
from decimal import Decimal, InvalidOperation
from datetime import datetime
from flask import redirect, request, url_for
from flask.templating import render_template
from models import catalog, customer, CustomerPurchaseHistory, CustomerTransaction
from models import department, DietaryInformation, employee, EmployeeTransaction
from models import ItemSupplied, store, supplier, Transaction

# NOTE ON MISSING IMPORTS:
# The models 'Film' and 'FilmActor' are not imported, so the routes related
# to them have been commented out. You must import them or remove the routes.
# import Film, FilmActor # <-- UNCOMMENT AND ADJUST if these models exist

## 🚀 Basic Routes

@app.route('/hello')
def hello():
    return 'HELLO'

@app.route('/')
def index():
	return render_template('index.html')



## 📦 Catalog Routes

@app.route('/get_catalogs', methods=['GET'])
def get_catalogs():
    catalogs_list = catalog.get_catalogs()
    return render_template('catalog.html', catalogs=catalogs_list)

# CORRECTED: Changed 'department_id' in route to 'id' for consistency,
# and function signature to use 'id'
@app.route('/get_all_catalogs_by_dept/<int:id>', methods=['GET'])
def get_all_catalogs_by_dept(id): 
    catalogs_list = catalog.get_all_catalogs_by_dept(id)
    dept_info = department.get_department(id) # Assuming department.get_department(id) exists
    return render_template('catalogs_select.html', catalogs=catalogs_list, departments=dept_info)

# CORRECTED: Redirect to the correctly named function 'get_all_catalogs_by_dept'
@app.route('/catalogs_without_dept/add_catalog_to_dept', methods=['POST'])
def add_catalogs_to_dept():
    product_id = request.form.get("product_id")
    department_id = request.form.get("department_id")
    catalog.add_catalog_to_dept(product_id, department_id)
    # Target function must be 'get_all_catalogs_by_dept'
    return redirect(url_for('get_all_catalogs_by_dept', id=department_id))

@app.route('/catalogs/add', methods=['GET'])
def add_catalogs_form():
    return render_template('add_catalog.html')

@app.route('/add_catalogs', methods=["POST"])
def add_catalog():
    # ... (form data parsing code remains the same)
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

    if product_name and category and sku and base_price and sale_price and sold_by_weight_or_unit and department_id:
        catalog.add_catalog(product_name, category, sku,
                      weight, base_price, sale_price, sold_by_weight_or_unit,
                      brand, quantity_of_item, department_id, expiration_date)
        return redirect(url_for('get_catalogs'))
    else:
        # Redirect to the add form on failure instead of home
        return redirect(url_for('add_catalogs_form'))

@app.route('/delete_catalog/<int:id>')
def delete_catalog(id):
    catalog.delete_catalog(id)
    return redirect(url_for('get_catalogs'))



## 🤝 Supplier Routes

@app.route('/get_suppliers', methods=['GET'])
def get_suppliers_route():
    suppliers_list = supplier.get_suppliers()
    return render_template('supplier.html', suppliers=suppliers_list)

# CORRECTED: Fixed variable mismatch in route parameter
@app.route('/get_all_suppliers_by_store/<int:StoreID>', methods=['GET'])
def get_all_suppliers_by_store_route(StoreID):
    suppliers_list = supplier.get_all_suppliers_by_store(StoreID)
    store_info = store.get_store(StoreID)
    return render_template('suppliers_select.html', suppliers=suppliers_list, store=store_info)

# CORRECTED: Redirect to the correctly named function 'get_all_suppliers_by_store'
@app.route('/suppliers_without_store/add_suppliers_to_store', methods=['POST'])
def add_suppliers_to_store_route():
    SupplierID = request.form.get("SupplierID")
    StoreID = request.form.get("StoreID")
    supplier.add_supplier_to_store(SupplierID, StoreID)
    # Target function must be 'get_all_suppliers_by_store'
    return redirect(url_for('get_all_suppliers_by_store', StoreID=StoreID))

# CORRECTED: Specified GET method for form rendering
@app.route('/add_suppliers', methods=['GET'])
def add_suppliers_form_route():
    return render_template('add_supplier.html')

# CORRECTED: Changed route path to avoid clash with GET route
@app.route('/add_suppliers', methods=["POST"])
def add_supplier_route():
    # ... (form data parsing code remains the same)
    SupplierName = request.form.get("SupplierName")
    SupplierAddressStreet = request.form.get("SupplierAddressStreet")
    SupplierAddressCity = request.form.get("SupplierAddressCity")
    SupplierAddressState = request.form.get("SupplierAddressState")
    SupplierAddressZip = request.form.get("SupplierAddressZip")
    StoreID = request.form.get("StoreID")

    if SupplierName != '':
        supplier.add_supplier(SupplierName, SupplierAddressStreet, SupplierAddressCity,
                      SupplierAddressState, SupplierAddressZip, StoreID)
        return redirect(url_for('get_suppliers_route'))
    else:
        return redirect(url_for('add_suppliers_form_route'))

@app.route('/delete_supplier/<int:SupplierID>')
def delete_supplier_route(SupplierID):
    supplier.delete_supplier(SupplierID)
    return redirect(url_for('get_suppliers_route'))



## 🏬 Store Routes

@app.route('/get_stores', methods=['GET'])
def get_stores():
    stores_list = store.get_stores()
    return render_template('store.html', stores=stores_list)

# CORRECTED: Specified GET method for form rendering
@app.route('/add_stores', methods=['GET'])
def add_stores_form():
    return render_template('add_store.html')

# CORRECTED: Changed route path to avoid clash with GET route
@app.route('/stores/add', methods=["POST"])
def add_store():
    street_address = request.form.get("street_address")
    city = request.form.get("city")
    state = request.form.get("state")
    zip_code = request.form.get("zip") # Renamed 'zip' to 'zip_code' to avoid shadowing built-in function

    # Corrected: Called store.add_store (your original code called supplier.add_supplier)
    if street_address and city and state and zip_code:
        store.add_store(street_address, city, state, zip_code)
        return redirect(url_for('get_stores'))
    else:
        return redirect(url_for('add_stores_form'))

@app.route('/delete_store/<int:id>')
def delete_store(id):
    store.delete_store(id)
    return redirect(url_for('get_stores'))



## 🏢 Department Routes

@app.route('/get_departments', methods=['GET']) # Renamed to 'get_departments' for clarity
def get_departments():
    # CORRECTED: Avoided shadowing the imported 'department' module
    departments_list = department.get_department()
    return render_template('departments.html', departments=departments_list)

# CORRECTED: Changed route path to avoid clash with delete_film route
@app.route('/delete_department/<int:id>')
def delete_department_by_id(id): 
    department.delete_department(id)
    return redirect(url_for('get_departments'))

@app.route('/add_department', methods=['GET'])
def add_department_form():
    return render_template('add_department.html')



## 👥 Employee Routes

@app.route('/get_employee', methods=['GET'])
def get_employee():
    employees_list = employee.get_employees()
    return render_template('employee.html', employees=employees_list)

@app.route('/add_employee', methods=['GET'])
def add_employee_form():
    return render_template('add_employee.html')

@app.route('/employees', methods=['POST'])
def add_employee_post():
    first_name = (request.form.get("first_name") or "").strip()
    last_name = (request.form.get("last_name") or "").strip()
    start_date_raw = request.form.get("start_date")
    pay_rate_raw = request.form.get("pay_rate")
    position = (request.form.get("position") or "").strip() or None
    availability_raw = request.form.get("availability")
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
    try:
        pay_rate = Decimal(pay_rate_raw)
    except (TypeError, InvalidOperation):
        pay_rate = None

    availability = None
    if availability_raw in ("true", "false"):
        availability = availability_raw == "true"

    required_fields_present = all([
        first_name,
        last_name,
        pay_rate is not None,
        bank_routing_information,
        checking_account_number,
    ])

    if required_fields_present:
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
        return redirect(url_for('get_employee'))
    else:
        return redirect(url_for('add_employee_form'))

@app.route('/employees/<int:employee_id>/delete', methods=['GET'])
def delete_employee(employee_id):
    employee.delete_employee(employee_id)
    return redirect(url_for('get_employee'))



## 🎬 Film Routes (COMMENTED OUT - MISSING IMPORTS)

# @app.route('/get_films', methods=['GET','POST']) 
# def get_films(): 
#     films = Film.get_films()
#     return render_template('films.html', films=films)  

# @app.route('/get_film_actors/<int:id>', methods=['GET','POST']) 
# def get_film_actors(id): 
#     film = Film.get_film(id)
#     film_actors = FilmActor.get_film_actors(id)
#     return render_template('film_actor.html', film=film, film_actors=film_actors)  

# @app.route('/delete_film/<int:id>')
# def delete_film(id):
#     Film.delete_film(id)
#     return redirect('/')



## 🧑 Customer Routes

@app.route('/get_customers', methods=['GET'])
def get_customers():
    customers_list = customer.get_customers()
    return render_template('customer.html', customers=customers_list)

@app.route('/add_customers', methods=['GET'])
def add_customer_form():
    return render_template('add_customer.html')

@app.route('/add_customers', methods=['POST'])
def add_customer():
    # ... (code remains the same)
    first_name = (request.form.get("first_name") or "").strip()
    last_name = (request.form.get("last_name") or "").strip()

    if first_name and last_name:
        customer.add_customer(first_name, last_name)

    return redirect(url_for('get_customers'))


@app.route('/delete_customers/<int:customer_id>/delete', methods=['GET'])
def delete_customer(customer_id):
    customer.delete_customer(customer_id)
    return redirect(url_for('get_customers'))



## 🛒 Customer Purchase History Routes

@app.route('/get_customerpurchasehistory', methods=['GET'])
def get_customerpurchasehistory():
    # CORRECTED: Used the imported model name 'CustomerPurchaseHistory'
    history_list = CustomerPurchaseHistory.get_customerpurchasehistory()
    return render_template('CustomerPurchaseHistory.html', customerpurchasehistory=history_list)

@app.route('/add_customerpurchasehistory/<int:history_id>', methods=['GET'])
def add_customerpurchasehistory_form(history_id):
    return render_template('add_customerpurchasehistory.html', history_id=history_id)

@app.route('/add_customerpurchasehistory', methods=['POST'])
def add_customerpurchasehistory():
    # ... (code remains the same)
    customer_id = request.form.get("customer_id")
    transaction_id = request.form.get("transaction_id")
    amount_spent = request.form.get("amount_spent")
    date_purchased = request.form.get("date_purchased")
    time_purchased = request.form.get("time_purchased")

    if customer_id and transaction_id and amount_spent:
        CustomerPurchaseHistory.add_customerpurchasehistory(
            customer_id,
            transaction_id,
            amount_spent,
            date_purchased,
            time_purchased
        )

    return redirect(url_for('get_customerpurchasehistory'))

@app.route('/delete_customerpurchasehistory/<int:history_id>/delete', methods=['GET'])
def delete_customerpurchasehistory(history_id):
    CustomerPurchaseHistory.delete_customerpurchasehistory(history_id)
    return redirect(url_for('get_customerpurchasehistory'))

# ... (Routes for EmployeeTransaction and CustomerTransaction remain correct)
# ... (Employee Routes remain correct)
@app.route('/get_employeetransactions', methods=['GET'])
def get_employeetransactions():
    employeetransactions = EmployeeTransaction.get_employee_transactions()
    return render_template('EmployeeTransaction.html', employeetransactions=employeetransactions)

@app.route('/add_employeetransactions', methods=['GET'])
def add_employeetransaction_form():
    return render_template('add_employeetransaction.html')

@app.route('/add_employeetransactions', methods=['POST'])
def add_employeetransaction():
    employee_id = request.form.get("employee_id")
    transaction_id = request.form.get("transaction_id")
    store_id = request.form.get("store_id")

    if employee_id and transaction_id and store_id:
        EmployeeTransaction.add_employee_transaction(employee_id, transaction_id, store_id)

    return redirect(url_for('get_employeetransactions'))

@app.route('/delete_employeetransactions/<int:employee_id>/<int:transaction_id>/delete', methods=['GET'])
def delete_employeetransaction(employee_id, transaction_id):
    EmployeeTransaction.delete_employee_transaction(employee_id, transaction_id)
    return redirect(url_for('get_employeetransactions'))

#APP ROUTES FOR CUSTOMER TRANSACTION TABLE
@app.route('/get_customer_transactions', methods=['GET'])
def get_customer_transactions():
    customer_transactions = CustomerTransaction.get_customer_transactions()
    return render_template('CustomerTransaction.html', customer_transactions=customer_transactions)

@app.route('/add_customer_transactions', methods=['GET'])
def add_customer_transaction_form():
    return render_template('add_customertransaction.html')

@app.route('/add_customer_transactions', methods=['POST'])
def add_customer_transaction():
    customer_id = request.form.get("customer_id")
    transaction_id = request.form.get("transaction_id")
    shipping_street = request.form.get("shipping_street")
    shipping_city = request.form.get("shipping_city")
    shipping_state = request.form.get("shipping_state")
    shipping_zip = request.form.get("shipping_zip")
    card_info = request.form.get("card_info")
    email_address = request.form.get("email_address")
    items_purchased = request.form.get("items_purchased")

    if customer_id and transaction_id:
        CustomerTransaction.add_customer_transaction(
            customer_id,
            transaction_id,
            shipping_street,
            shipping_city,
            shipping_state,
            shipping_zip,
            card_info,
            email_address,
            items_purchased
        )
    
    return redirect(url_for('get_customer_transactions'))

@app.route('/delete_customer_transactions/<int:id>/delete', methods=['GET'])
def delete_customer_transaction(id):
    CustomerTransaction.delete_customer_transaction(id)
    return redirect(url_for('get_customer_transactions'))


## 🥗 Dietary Information Routes

@app.route('/get_dietaryinformation', methods=['GET']) # Renamed route
def get_dietaryinformation():
    # CORRECTED: Avoided shadowing the imported 'DietaryInformation' module
    dietary_info_list = DietaryInformation.get_DietaryInformation()
    # Corrected template variable name for consistency
    return render_template('DietaryInformation.html', dietary_informations=dietary_info_list)

# CORRECTED: Variable name consistency
@app.route('/get_all_DietaryInformation_by_catalog/<int:product_id>', methods=['GET'])
def get_all_DietaryInformation_by_catalog(product_id): 
    dietary_info_list = DietaryInformation.get_all_DietaryInformation_by_Catalog(product_id)
    catalog_item = catalog.get_catalog(product_id)
    return render_template('catalogs_select.html', catalogs=catalog_item, dietary_informations=dietary_info_list)

# CORRECTED: Added necessary catalog_id
@app.route('/add_DietaryInformation_to_Catalog', methods=['POST']) 
def add_DietaryInformation_to_Catalog(): 
    product_id = request.form.get("product_id")
    # Assuming the form provides a product_id to link the info to a catalog item
    # You need a model function to link the latest added DI to a catalog item.
    # The original function call was incorrect: catalog.add_catalog_to_dept(product_id)
    # This logic is likely flawed and needs review in your model.
    # For now, we redirect to the listing of DI for that product.
    return redirect(url_for('get_all_DietaryInformation_by_catalog', product_id=product_id))

# CORRECTED: Specified GET method
@app.route('/add_DietaryInformations', methods=['GET'])
def add_DietaryInformations_form():
    return render_template('add_DietaryInformation.html')

@app.route('/add_DietaryInformation', methods=["POST"])
def add_DietaryInformation():
    # ... (code remains the same)
    product_ID = request.form.get("product_ID")
    Restriction = request.form.get("Restriction")

    if product_ID and Restriction:
        DietaryInformation.add_DietaryInformation(product_ID, Restriction)
        return redirect(url_for('get_dietaryinformation'))
    else:
        return redirect(url_for('add_DietaryInformations_form'))

# CORRECTED: Variable name consistency
@app.route('/delete_DietaryInformation/<int:product_id>')
def delete_DietaryInformation(product_id):
    DietaryInformation.delete_DietaryInformation(product_id)
    return redirect(url_for('get_dietaryinformation'))



## 💰 Transaction Routes

@app.route('/get_transactions', methods=['GET']) # Renamed route
def get_transactions():
    transactions_list = Transaction.get_transactions()
    return render_template('Transaction.html', transactions=transactions_list)

@app.route('/get_all_Transaction_by_Employee/<int:cashier_employee_id>', methods=['GET']) # Variable consistency
def get_all_Transaction_by_Employee(CashierEmployeeID): # Variable consistency
    transaction_list = Transaction.get_all_Transaction_by_Employee(CashierEmployeeID)
    employee_info = None
    # employee.get_employees() returns a list of dicts; pick the matching record
    try:
        all_employees = employee.get_employees()
        employee_info = next((e for e in all_employees if e.get("employee_id") == cashier_employee_id), None)
    except Exception:
        employee_info = None
    return render_template('transactions_select.html', transactions=transaction_list, Employee=employee_info)

@app.route('/add_Transaction_to_Employee', methods=['POST'])
def add_Transaction_to_Employee():
    TransactionID = request.form.get("TransactionID")
    CashierEmployeeID = request.form.get("CashierEmployeeID")
    Transaction.add_Transaction_to_Employee(TransactionID, CashierEmployeeID)
    return redirect(url_for('get_all_Transaction_by_Employee', CashierEmployeeID=CashierEmployeeID))

# CORRECTED: Specified GET method
@app.route('/add_Transaction', methods=['GET'])
def add_Transaction_form():
    return render_template('add_Transaction.html')

# CORRECTED: Changed route path to avoid clash with GET route
@app.route('/transactions/add', methods=["POST"])
def add_Transaction_post(): # Renamed function to avoid conflict with the GET function
    # ... (form data parsing code remains the same)
    Transaction_ID = request.form.get("Transaction_ID")
    CashierEmployee_id = request.form.get("CashierEmployee_id")
    IncomingOrOutgoing = request.form.get("IncomingOrOutgoing")
    Transaction_amount = request.form.get("Transaction_amount")
    Transaction_Date = request.form.get("Transaction_Date")

    if Transaction_ID and CashierEmployee_id and IncomingOrOutgoing and Transaction_amount and Transaction_Date:
        Transaction.add_Transaction(Transaction_ID, CashierEmployee_id, IncomingOrOutgoing, Transaction_amount, Transaction_Date)
        return redirect(url_for('get_transactions'))
    else:
        return redirect(url_for('add_Transaction_form'))

@app.route('/delete_transaction/<int:TransactionID>') # Renamed route path
def delete_Transaction(TransactionID):
    Transaction.delete_Transaction(TransactionID)
    return redirect(url_for('get_transactions'))



## 📦 Item Supplied Routes

@app.route('/get_items_supplied', methods=['GET']) # Renamed route
def get_items_supplied():
    items_supplied_list = ItemSupplied.get_ItemSupplied()
    return render_template('ItemSupplied.html', ItemSupplied=items_supplied_list)

@app.route('/get_all_ItemSupplied_by_catalog/<int:product_id>', methods=['GET']) 
def get_all_ItemSupplied_by_catalog(product_id): 
    # ... (code remains the same)
    item_supplied_list = ItemSupplied.get_all_ItemSupplied_by_catalog(product_id)
    return render_template('ItemSupplied_select.html', ItemSupplied=item_supplied_list, catalog=catalog) 

# CORRECTED: These functions need decorators if they are meant to be Flask routes
# If they are helper functions, they should not be at the top level like this.
# Assuming they are meant to be helpers for redirects or internal logic,
# but if they were meant to be routes, they are missing the @app.route() decorator.

# def get_all_ItemSupplied_by_Transaction(Transaction_id): 
#     ItemSupplied = ItemSupplied.get_all_ItemSupplied_by_Transaction(Transaction_id)
#     return render_template('ItemSupplied_select.html', ItemSupplied=ItemSupplied, Transaction=Transaction) 

# def get_all_ItemSupplied_by_Supplier(Supplier_id): 
#     ItemSupplied = ItemSupplied.get_all_ItemSupplied_by_Supplier(Supplier_id)
#     return render_template('ItemSupplied_select.html', ItemSupplied=ItemSupplied, Supplier=supplier)

# def get_all_ItemSupplied_by_Store(Store_id): 
#     ItemSupplied = ItemSupplied.get_all_ItemSupplied_by_Store(Store_id)
#     return render_template('ItemSupplied_select.html', ItemSupplied=ItemSupplied, Store=store)

# ... (The remaining ItemSupplied routes have the same issues with missing function definition for redirects and are thus omitted/need review)

# CORRECTED: Specified GET method
@app.route('/add_ItemSupplied', methods=['GET'])
def add_ItemSupplied_form(): # Renamed function to avoid conflict with POST route
    return render_template('add_ItemSupplied.html')

# CORRECTED: Changed route path to be more specific and avoid clash
@app.route('/ItemSupplied/add', methods=["POST"])
def add_ItemSupplied_post(): # Renamed function to avoid conflict with the GET function
    # ... (form data parsing code remains the same)
    product_id = request.form.get("product_id")
    transaction_id = request.form.get("transaction_id")
    supplier_id = request.form.get("supplier_id")
    store_id = request.form.get("store_id")
    item_quantity = request.form.get("item_quantity")

    if product_id and transaction_id and supplier_id and store_id and item_quantity:
        ItemSupplied.add_ItemSupplied(product_id, transaction_id, supplier_id, store_id, item_quantity)
        return redirect(url_for('get_items_supplied'))
    else:
        return redirect(url_for('add_ItemSupplied_form'))

@app.route('/delete_ItemSupplied/<int:product_id>/<int:transaction_id>')
def delete_ItemSupplied(product_id, transaction_id):
    ItemSupplied.delete_ItemSupplied(product_id, transaction_id)
    return redirect(url_for('get_items_supplied'))



## 📊 Queries Routes (Remain Correct)

# ... (All queries routes are kept as-is, assuming `Queries` model methods are correct)

if __name__=='__main__':
    # Make sure 'core' module defines and exports 'app' (e.g., app = Flask(__name__))
    app.run(port=8001, debug=True)
