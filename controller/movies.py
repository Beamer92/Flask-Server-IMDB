import model.movies as model
from app import InvalidUsage


def getAll():
    return model.getAll()

def create(data):
    if data.get('name') is not None and data.get('description') is not None and  data.get('release_date') is not None and  data.get('rating') is not None:
        if data.get('poster_url') is None:
            data['poster_url'] = ''
        return model.create(data)
    else:
        raise InvalidUsage('POST movie is missing data')

def getOne(movieId):
    if movieId is not None:
        return model.getOne(movieId)
    else:
        raise InvalidUsage('GetOne requires Movie Id')

def update(movieId, data):
    result = model.getOne(movieId)
    if data.get('name'):
        result['name'] = data['name']
    if data.get('description'):
        result['description'] = data['description']
    if data.get('release_date'):
        result['release_date'] = data['release_date']
    if data.get('rating'):
        result['rating'] = data['rating']
    if data.get('poster_url'):
        result['poster_url'] = data['poster_url']

    return model.update(movieId, result)


def remove(movieId):

    return model.remove(movieId)


def getActors(movieId):

    return model.getActors(movieId)

def addActorToMovie(movieId, actorId):

    return model.addActorToMovie(movieId, actorId)

def removeActorFromMovie(movieId, actorId):

    return model.removeActorFromMovie(movieId, actorId)

