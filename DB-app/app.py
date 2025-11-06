from core import app
from flask import redirect, request, url_for 
from flask.templating import render_template
from models import Actor, Film, FilmActor, Queries

# A decorator used to tell the application 
# which URL is associated with which function 
@app.route('/hello')	 
def hello(): 
	return 'HELLO'

# APP ROUTE TO RENDER HOME PAGE WITH LINKS
@app.route('/')
def index():
	return render_template('index.html')

# APP ROUTE TO GET RESULTS FOR SELECT QUERY 
@app.route('/get_actors', methods=['GET']) 
def get_results(): 
	actors = Actor.get_actors()
	return render_template('actors.html', actors=actors) 

@app.route('/get_actors_not_in_film/<int:id>', methods=['GET']) 
def get_actors_not_in_film(id): 
	actors = FilmActor.get_actors_not_in_film(id)
	film = Film.get_film(id)
	return render_template('actors_select.html', film=film, actors=actors)  

@app.route('/get_actors_not_in_film/add_actor_to_film', methods=['POST']) 
def add_actors_not_in_film(): 
	actor_id = request.form.get("actor_id")
	film_id = request.form.get("film_id")
	FilmActor.add_actor_to_film(film_id, actor_id)
	return redirect (url_for('get_film_actors', id=film_id))  

# APP ROUTE TO RENDER FORM TO ADD ACTOR DATA
@app.route('/add_actors')
def add_actors():
	return render_template('add_actor.html')

# APP ROUTE TO CALL FUNCTION TO ADD ACTOR
@app.route('/add', methods=["POST"])
def add_actor():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")

	# call model function that will store data as a row in our datatable
	if first_name != '' and last_name != '':
		Actor.add_actor(first_name, last_name)
		return redirect('/')
	else:
		return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE ACTOR
@app.route('/delete_actor/<int:id>')
def delete_actor(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	Actor.delete_actor(id)
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


