import model.movies as model

def getAll():
    return model.getAll()

def create(data):
    movieData = {}
    return model.create(movieData)

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

