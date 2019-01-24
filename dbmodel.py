import db from app

class Actors(db.Model):
    __tablename__ = 'actorsq'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    biography = db.Column(db.Text, unique=False, nullable=False)
    profile_url = db.Column(db.String(200), unique=False, nullable=True)
    birth_date = db.Column(db.DateTime,unique=False , nullable=False)
    created_at = db.Column(db.DateTime, unique=False)
    updated_at = db.Column(db.DateTime, unique=False)

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    release_date = db.Column(db.DateTime,unique=False , nullable=False)
    rating = db.Column(db.String(5), unique=False, nullable=False)
    poster_url = db.Column(db.String(200), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, unique=False)
    updated_at = db.Column(db.DateTime, unique=False)


class MovAct(db.Model):
    __tablename__ = 'movies_actors'
    id = db.Column(db.Integer, primary_key=True)
    movies_id = db.Column(db.Integer, ForeignKey('actors.id'), nullable=False)
    actors_id = db.Column(db.Integer, ForeignKey('movies.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False)
 