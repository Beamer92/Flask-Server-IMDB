#knex.schema.createTable('movies', (table) => {
#     table.increments()
#     table.string('name').notNull()
#     table.text('description').notNull()
#     table.timestamp('release_date').notNull()
#     table.string('rating').notNull()
#     table.string('poster_url')
#     table.timestamps(true, true)

from dbmodel import Actors, Movies, MovAct
from app import InvalidUsage, db

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

    return

def addActorToMovie(movieId, actorId):

    return 

def removeActorFromMovie(movieId, actorId):

    return 