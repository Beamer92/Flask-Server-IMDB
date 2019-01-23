from flask import Flask, request, jsonify
app = Flask(__name__)
import controller.movies as movies
import controller.actors as actors
#note that __name__ is two underscores on each side

########### MOVIES ROUTES##############
@app.route('/movies', methods=['GET', 'POST'])
def moviesGP():
    if request.method == 'GET':
        result = movies.getAll()  
        return jsonify(result)
    elif request.method == 'POST':
        data = request.form
        result = movies.create(data)
        return jsonify(result)

@app.route('/movies/<movieId>', methods=['GET', 'PUT', 'DELETE'])
def movie(movieId):
    if request.method == 'GET':
        result = movies.getOne(movieId)
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.form
        result = movies.update(movieId, data)
        return jsonify(result)
    elif request.method == 'DELETE':
        result = movies.remove(movieId)
        return jsonify(result)

@app.route('/movies/<movieId>/actors', methods=['GET'])
def getActors(movieId):
    result = movies.getActors(movieId)
    return jsonify(result)

@app.route('/movies/<movieId>/actors/add', methods=['PATCH'])
def addActorToMovie(movieId):
    if request.form.actorId:
        result = movies.addActorToMovie(movieId, request.form.actorId)
        return jsonify(result)
    else:
        return {status: 400, message: "Bad PATCH Request"}

@app.route('/movies/<movieId>/actors/remove', methods=['PATCH'])
def removeActorFromMovie(movieId):
    if request.form.actorId:
        result =  movies.removeActorFromMovie(movieId, request.form.actorId)
        return jsonify(result)
    else:
        return {status: 400, message: "Bad PATCH Request"}

######## ACTORS ROUTES##############
@app.route('/actors', methods=['GET', 'POST'])
def actorsGP():
    if request.method == 'GET':
        result = actors.getAll()  
        return jsonify(result)
    elif request.method == 'POST':
        data = request.form
        result = actors.create(data)
        return jsonify(result)

@app.route('/actors/<actorId>', methods=['GET', 'PUT', 'DELETE'])
def actor(actorId):
    if request.method == 'GET':
        result = actors.getOne(actorId)
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.form
        result = actors.update(actorId, data)
        return jsonify(result)
    elif request.method == 'DELETE':
        result = actors.remove(actorId)
        return jsonify(result)

@app.route('/actors/<actorId>/movies', methods=['GET'])
def getMovies(actorId):
    result = actors.getMovies(actorId)
    return jsonify(result)

@app.route('/actors/<actorId>/movies/add', methods=['PATCH'])
def addMovieToActor(actorId):
    if request.form.actorId:
        result = actors.addMovietoActor(actorId, request.form.movieId)
        return jsonify(result)
    else:
        return {status: 400, message: "Bad PATCH Request"}

@app.route('/actors/<actorId>/movies/remove', methods=['PATCH'])
def removeMovieFromActor(actorId):
    if request.form.actorId:
        result =  actors.removeMovieFromActor(actorId, request.form.movieId)
        return jsonify(result)
    else:
        return {status: 400, message: "Bad PATCH Request"}

