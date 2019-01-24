#knex.schema.createTable('movies', (table) => {
#     table.increments()
#     table.string('name').notNull()
#     table.text('description').notNull()
#     table.timestamp('release_date').notNull()
#     table.string('rating').notNull()
#     table.string('poster_url')
#     table.timestamps(true, true)

def getMovies():

    pass

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