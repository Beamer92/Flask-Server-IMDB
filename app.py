from flask import Flask, request, jsonify
app = Flask(__name__)
import controller.movies as movies
#note that __name__ is two underscores on each side

@app.route('/movies', methods=['GET', 'POST'])
def movies():
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



#actors
# router.get('/', actorsController.getAll)
# router.get('/:actorId', actorsController.getOne)
# router.post('/', actorsController.create)
# router.put('/:actorId', actorsController.update)
# router.delete('/:actorId', actorsController.remove)

# router.get('/:actorId/movies', actorsController.getAllMoviesForAnActor)
# router.patch('/:actorId/movies/add', actorsController.addMovieToActor)
# router.patch('/:actorId/movies/remove', actorsController.removeMovieFromActor)


