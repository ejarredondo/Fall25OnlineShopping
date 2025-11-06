from sqlalchemy import DateTime
from core import db
from sqlalchemy.sql import func

# Models
class Actor(db.Model):
 
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    
class Film(db.Model):
    
    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    release_year = db.Column(db.Integer, nullable=True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    
class FilmActor(db.Model):

    actor_id = db.Column(db.Integer, db.ForeignKey('actor.actor_id'), primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.film_id'), primary_key=True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
