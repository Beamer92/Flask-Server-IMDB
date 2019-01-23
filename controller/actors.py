import model.actors as model

def getAll():
    return model.getAll()

def create(data):
    actorData = {}
    return model.create(actorData)

def getOne(actorId):

    return model.getOne(actorId)

def update(actorId, data):

    return model.update(actorId, data)


def remove(actorId):

    return model.remove(actorId)


def getMovies(actorId):

    return model.getMovies(actorId)

def addMovietoActor(actorId, movieId):

    return model.addMovieToActor(actorId, movieId)

def removeMovieFromActor(actorId, movieId):

    return model.removeMovieFromActor(actorId, movieId)

