from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

films=[{
    "ID":1,
    "Title":"Harry Potter",
    "Rating":10,
    "Director":"David Yates",
    "Votes":0
},
{
    "ID":2,
    "Title":"The Avengers",
    "Rating":9,
    "Director":"Joss Whedon",
    "Votes":0
},
{
    "ID":3,
    "Title":"Superman Returns",
    "Rating":5,
    "Director":"Bryan Singer",
    "Votes":0
}]

nextID=4

@app.route('/films')
def getAll():
    return jsonify(films)
#curl "http://127.0.0.1:5000/films"

@app.route('/films/<int:id>')
def findID(id):
    filmCheck = list(filter(lambda f: f['ID']==id, films))
    if len(filmCheck)==0:
        abort(404)
        #return jsonify({}), 204
    return jsonify(filmCheck[0])

#curl "http://127.0.0.1:5000/films/3"

@app.route('/films', methods=['POST'])
def createFilm():
    global nextID
    if not request.json:
        abort(400)
    #Check that properly formatted add code here
    film={
        "ID":nextID,
        "Title": request.json['Title'],
        "Rating": request.json['Rating'],
        "Director": request.json['Director'],
        "Votes": 0
    }
    nextID += 1
    films.append(film)
    return jsonify(film)
#curl -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"King Kong\",\"Rating\":\"6\",\"Director\":\"Peter Jackson\"}" http://127.0.0.1:5000/films

@app.route('/films/<int:id>', methods=['PUT'])
def updateFilm(id):
    changeFilm = list(filter(lambda f: f['ID']==id, films))
    if (len(changeFilm) ==0):
        abort(404)
    changeFilm = changeFilm[0]
    
    if not request.json:
        abort(400)

    requestJson = request.json
    if 'Title' in requestJson and type(requestJson['Title']) is not str:
        abort(400)
    if 'Rating' in requestJson and type(requestJson['Rating']) is not int:
        abort(400)
    if 'Director' in requestJson and type(requestJson['Director']) is not str:
        abort(400)
    
    if 'Title' in requestJson:
        changeFilm['Title'] = requestJson['Title']
    
    if 'Rating' in requestJson:
        changeFilm['Rating'] = requestJson['Rating']
    
    if 'Director' in requestJson:
        changeFilm['Director'] = requestJson['Director']
    
    return jsonify(changeFilm)
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"King Kong\",\"Director\":\"Peter Jackson\",\"Rating\":3}" http://127.0.0.1:5000/films/1

@app.route('/films/<int:id>', methods=['DELETE'])
def deleteFilm(id):
    deleteFilm = list(filter(lambda f: f['ID']==id, films))
    if (len(deleteFilm) ==0):
        abort(404)
    films.remove(deleteFilm[0])
    return jsonify({"done":True})

@app.route('/votes/<int:id>', methods=['POST'])
def addVote(id):
    foundFilm = list(filter(lambda f: f['ID']==id, films))
    if len(foundFilm)==0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'Votes' in request.json or type(request.json['Votes']) is not int:
        abort(401)
    updatedVote = request.json['Votes']

    foundFilm[0]['Votes'] += updatedVote
    
    return jsonify(foundFilm[0])

@app.route('/votes/leaderboard')
def getLeaderBoard():
    films.sort(key=lambda f: f['Votes'], reverse=True)
    return jsonify(films)

if __name__ == '__main__':
    app.run(debug= True)