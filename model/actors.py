from dbmodel import Actors, Movies, MovAct
from app import InvalidUsage, db
from sqlalchemy.sql import text
import json

def getAll():
    result = Actors.query.all()
    if result is not None:
        return Actors.serialize_list(result)
    else:
        raise InvalidUsage('Error, No Actors', status_code=404)

def create(data):
    actor = Actors(data['name'], data['biography'], data['profile_url'], data['birth_date'])
    db.session.add(actor)
    db.session.commit()
    db.session.refresh(actor)
    return actor.id


def getOne(actorId):
    result = Actors.query.get(actorId)
    if result is not None:
        return Actors.toDict(result)
    else:
        raise InvalidUsage('Error, Actor Not Found', status_code=404)


def update(actorId, data):
    try:
        db.session.query(Actors).\
        filter(Actors.id == ActorId).\
        update({'name': data['name'], 'biography': data['biography'], 'profile_url': data['profile_url'],'birth_date': data['birth_date']})
        db.session.commit()  
        db.session.flush()
        return 'Movie Has Been Updated!'  
    except:
        raise InvalidUsage('Error, update failed', status_code=400)

def remove(actorId):
    try:
        db.session.query(Actors).filter(Actors.id == actorId).delete()
        db.session.commit()
        return 'Movie Has Been Deleted'
    except:
        raise InvalidUsage('Error, delete failed', status_code=400)

def getMovies(actorId):
    sql = ('select movies.*, movies_actors.role from actors\
    inner join movies_actors on actors.id = movies_actors.actors_id\
    inner join movies on movies.id = movies_actors.movies_id\
    where actors.id = %s' % actorId)
    result = db.engine.execute(sql)
    if result is not None:
        return json.dumps([dict(r) for r in result], default=str)
    else:
        raise InvalidUsage('Error Occured getting Movies for that Actor', status_code=404)

