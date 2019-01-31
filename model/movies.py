from dbmodel import Actors, Movies, MovAct
from app import InvalidUsage, db
from sqlalchemy.sql import text
import json

def getAll():
    result = Movies.query.all()
    if result is not None:
        return Movies.serialize_list(result)
    else:
        raise InvalidUsage('Error, No Movies', status_code=404)

def create(data):
    movie = Movies(data['name'], data['description'], data['release_date'], data['rating'], data['poster_url'])
    db.session.add(movie)
    db.session.commit()
    db.session.refresh(movie)
    return movie.id
    
def getOne(movieId):
    result = Movies.query.get(movieId)
    if result is not None:
        return Movies.toDict(result)
    else:
        raise InvalidUsage('Error, Movie Not Found', status_code=404)

def update(movieId, data):
    try:
        db.session.query(Movies).\
        filter(Movies.id == movieId).\
        update({'name': data['name'], 'description': data['description'], 
		'release_date': data['release_date'], 'rating': data['rating'],'poster_url': data['poster_url']})

        db.session.commit()
        db.session.flush()
        return 'Movie has been updated!'
    except:
        raise InvalidUsage('Error, update failed', status_code=400)
    

def remove(movieId):
    try:
        db.session.query(Movies).filter(Movies.id == movieId).delete()
        db.session.commit()
        return 'Movie has been deleted!'
    except:
        raise InvalidUsage('Error, delete failed', status_code=400)


def getActors(movieId):
    sql = ('select actors.*, movies_actors.role from movies\
     inner join movies_actors on movies.id = movies_actors.movies_id\
     inner join actors on actors.id = movies_actors.actors_id\
     where movies.id = %s' % movieId)
    result = db.engine.execute(sql)
    if result is not None:
        return json.dumps([dict(r) for r in result], default=str)
    else:
        raise InvalidUsage('Error Occured', status_code=404)

def addActorToMovie(movieId, actorId, role):
    try:
        role = MovAct(movieId, actorId, role)
        db.session.add(role)
        db.session.commit()
        db.session.refresh(role)
        return role.role
    except:
        raise InvalidUsage('Error, PATCH failed', status_code=400)

def removeActorFromMovie(movieId, actorId):
    try:
        # db.session.query(MovAct).filter(MovAct.movies_id == movieId and MoveAct.actors_id == actorId).delete()
        # db.session.commit()
        # The above does not work and deletes all actors from that movie...
        #  no idea why as it's the only format for multiple WHERE paramaters that doesn't throw an error
        sql = ('delete from movies_actors where movies_actors.movies_id = %s and movies_actors.actors_id = %s' % (movieId, actorId))
        result = db.engine.execute(sql)
        if result is not None:
            return 'Actor has been deleted from that movie!'
        else:
            raise InvalidUsage('Error Occured', status_code=404)
    except:
        raise InvalidUsage('Error, PATCH REMOVE failed', status_code=400)
