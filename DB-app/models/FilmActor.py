from sqlalchemy import func, select
from models.schemas import Film, Actor, FilmActor
from core import ma, db

def get_film_actors(id): 
    actors = db.session.query(Actor
                ).join(FilmActor, FilmActor.actor_id == Actor.actor_id
                ).filter(FilmActor.film_id == id)
    
    return actors

def get_actors_not_in_film(id): 
    subquery = db.session.query(FilmActor.film_id
                ).filter(FilmActor.film_id == id
                ).subquery()
    actors = db.session.query(Actor
        ).filter(FilmActor.film_id.not_in(select(subquery)))
    return actors

def add_actor_to_film(film_id, actor_id):
    a = FilmActor(actor_id=actor_id, film_id=film_id, last_update=func.now())
    db.session.add(a)
    db.session.commit()

     
class FilmActorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FilmActor

film_actors_schema = FilmActorSchema()
#films_schema = FilmSchema(many=True)