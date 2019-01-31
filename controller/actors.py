import model.actors as model
import model.movies as movieModel
from app import InvalidUsage

def getAll():
    return model.getAll()

def create(data):
    if data.get('name') is not None and data.get('biography') is not None and data.get('birth_date') is not None:
        if data.get('profile_url') is None:
            data['profile_url'] = ''
        return model.create(data)
    else:
        raise InvalidUsage('POST actor is missing data')

def getOne(actorId):
    if actorId is not None:
        return model.getOne(actorId)
    else:
        raise InvalidUsage('GetOne requires Actor Id')

def update(actorId, data):
    result = model.getOne(actorId)
    if data.get('name'):
        result['name'] = data['name']
    if data.get('biography'):
        result['biography'] = data['biography']
    if data.get('profile_url'):
        result['profile_url'] = data['profile_url']
    if data.get('birth_date'):
        result['birth_date'] = data['birth_date']
    return model.update(actorId, result)

def remove(actorId):
    return model.remove(actorId)


def getMovies(actorId):
    return model.getMovies(actorId)

def addMovietoActor(actorId, data):
    if data.get('movieId') and data.get('role'):
        movieId = data.get('movieId')
        role = data.get('role')
        actorRes = model.getOne(actorId)
        movieRes = movieModel.getOne(movieId)
        if actorRes is not None and movieRes is not None:
            return movieModel.addActorToMovie(movieId, actorId, role)
        else:
            raise InvalidUsage('Error, could not find either Actor or Movie')
    else:
        raise InvalidUsage('Error, Actor and Role are required')


def removeMovieFromActor(actorId, data):
    if data.get('movieId'):
        movieId = data.get('movieId')
        actorRes = model.getOne(actorId)
        movieRes = movieModel.getOne(movieId)
        if actorRes is not None and movieRes is not None:
            return movieModel.removeActorFromMovie(movieId, actorId)
        else:
            raise InvalidUsage('Error, could not find either Actor or Movie')
    else:
        raise InvalidUsage('Error, Actor is required')

