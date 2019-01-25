#knex.schema.createTable('movies', (table) => {
#     table.increments()
#     table.string('name').notNull()
#     table.text('description').notNull()
#     table.timestamp('release_date').notNull()
#     table.string('rating').notNull()
#     table.string('poster_url')
#     table.timestamps(true, true)

from dbmodel import Actors, Movies, MovAct
from app import InvalidUsage

def getAll():
    result = Movies.query.all()
    if result is not None:
        return Movies.serialize_list(result)
    else:
        raise InvalidUsage('Error, No Movies', status_code=400)

def create(data):

    pass

def getOne(movieId):

    return 

def update(movieId, data):

    return


def remove(movieId):

    return


def getActors(movieId):

    return

def addActorToMovie(movieId, actorId):

    return 

def removeActorFromMovie(movieId, actorId):

    return 