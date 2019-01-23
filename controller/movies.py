import model.movies as model

#knex.schema.createTable('movies', (table) => {
#     table.increments()
#     table.string('name').notNull()
#     table.text('description').notNull()
#     table.timestamp('release_date').notNull()
#     table.string('rating').notNull()
#     table.string('poster_url')
#     table.timestamps(true, true)

def getAll():
    return model.getAll()

def create(data):
    if data.name is not None and data.description is not None and data.release_date is not None and data.rating is not None:
        movieData = {}
        return model.create(movieData)
    else:
        return "error" ##error messages still need to be looked up

def getOne(movieId):

    return model.getOne(movieId)

def update(movieId, data):

    return model.update(movieId, data)


def remove(movieId):

    return model.remove(movieId)


def getActors(movieId):

    return model.getActors(movieId)

def addActorToMovie(movieId, actorId):

    return model.addActorToMovie(movieId, actorId)

def removeActorFromMovie(movieId, actorId):

    return model.removeActorFromMovie(movieId, actorId)
