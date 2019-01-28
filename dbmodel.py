from app import db
from sqlalchemy import inspect

class Actors(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    biography = db.Column(db.Text, unique=False, nullable=False)
    profile_url = db.Column(db.String(200), unique=False, nullable=True)
    birth_date = db.Column(db.DateTime,unique=False , nullable=False)
    created_at = db.Column(db.DateTime, unique=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, unique=False, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, name, biography, profile_url, birth_date):
        self.name = name
        self.biography = biography
        self.profile_url = profile_url
        self.birth_date = birth_date

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    @staticmethod
    def serialize_list(l):
        return [m.toDict() for m in l]

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    release_date = db.Column(db.DateTime,unique=False , nullable=False)
    rating = db.Column(db.String(5), unique=False, nullable=False)
    poster_url = db.Column(db.String(200), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, unique=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, unique=False, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, name, description, release_date, rating, poster_url):
        self.name = name
        self.description = description
        self.release_date = release_date
        self.rating = rating
        self.poster_url = poster_url

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    @staticmethod
    def serialize_list(l):
        return [m.toDict() for m in l]


class MovAct(db.Model):
    __tablename__ = 'movies_actors'
    id = db.Column(db.Integer, primary_key=True)
    movies_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)
    actors_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, movies_id, actors_id, role):
        self.movies_id = movies_id
        self.actors_id = actors_id
        self.role = role

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    @staticmethod
    def serialize_list(l):
        return [m.toDict() for m in l]
 