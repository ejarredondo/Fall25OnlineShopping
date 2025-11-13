
from sqlalchemy import func
from models.schemas import Film
from core import ma, db

def get_films(): 
    all_films = Film.query.all()
    return films_schema.dump(all_films)

def get_film(id):
    film = Film.query.get(id)
    return film

def add_film(first_name, last_name):
    a = Film(first_name=first_name, last_name=last_name, last_update=func.now())
    db.session.add(a)
    db.session.commit()

def delete_film(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	data = Film.query.get(id)
	db.session.delete(data)
	db.session.commit()
     
class FilmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Film

film_schema = FilmSchema()
films_schema = FilmSchema(many=True)

