from core import app
from decimal import Decimal, InvalidOperation
from datetime import datetime
from flask import redirect, request, url_for 
from flask.templating import render_template
from models import catalog, customer, customerpurchasehistory, customertransaction, department, DietaryInfo, employee, employeetransaction, ItemSupllied, store, supplier, Transaction

# A decorator used to tell the application 
# which URL is associated with which function 
@app.route('/hello')	 
def hello(): 
	return 'HELLO'

# APP ROUTE TO RENDER HOME PAGE WITH LINKS
@app.route('/')
def index():
	return render_template('index.html')

# APP ROUTE TO GET RESULTS FOR catalog SELECT QUERY 
@app.route('/get_catalogs', methods=['GET']) 
def get_results(): 
	catalogs = catalog.get_catalogs()
	return render_template('catalog.html', catalogs=catalogs) 

# APP ROUTE TO RENDER FORM TO ADD ACTOR DATA
@app.route('/add_catalogs')
def add_catalogs():
	return render_template('add_catalog.html')

# APP ROUTE TO CALL FUNCTION TO ADD ACTOR
@app.route('/add', methods=["POST"])
def add_actor():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	#first_name = request.form.get("first_name")
	#last_name = request.form.get("last_name")

	# call model function that will store data as a row in our datatable
	#if first_name != '' and last_name != '':
	#	catalog.add_catalog(first_name, last_name)
	#	return redirect('/')
	#else:
	#	return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE ACTOR
@app.route('/delete_catalog/<int:id>')
def delete_catalog(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	catalog.delete_catalog(id)
	return redirect('/')

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
