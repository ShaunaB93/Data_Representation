from flask import Flask, jsonify, request, abort, session, render_template, redirect, url_for
from filmDAO import filmDAO

app = Flask(__name__, static_url_path='', static_folder='.')
#app = Flask(__name__)

@app.route('/')
def login():
    return render_template("LoginPage.html")


@app.route('/films')
def getAll():
    filmResult = filmDAO.getAll()
    return jsonify(filmResult)
#curl "http://127.0.0.1:5000/films"

@app.route('/films/<int:id>')
def findID(id):
    foundFilm = filmDAO.findByID(id)
    return jsonify(foundFilm)

#curl "http://127.0.0.1:5000/films/3"

@app.route('/films', methods=['POST'])
def createFilm():
    global nextID
    if not request.json:
        abort(400)

    film={
        #"ID":nextID,
        "Title": request.json['Title'],
        "Rating": request.json['Rating'],
        "Director": request.json['Director'],
        "Votes": request.json['Votes']
    }
    
    filmValue = (film['Title'], film['Rating'], film['Director'], film['Votes'])
    updatedID = filmDAO.create(filmValue)
    film['ID'] = updatedID
    return jsonify(film)
#curl -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"King Kong\",\"Rating\":\"6\",\"Director\":\"Peter Jackson\"}" http://127.0.0.1:5000/films

@app.route('/films/<int:id>', methods=['PUT'])
def updateFilm(id):
    #changeFilm = list(filter(lambda f: f['ID']==id, films))
    changeFilm = filmDAO.findByID(id)
    if not changeFilm:
        abort(404)
    
    if not request.json:
        abort(400)

    requestJson = request.json
    if 'Title' in requestJson and type(requestJson['Title']) is not str:
        abort(400)
    if 'Rating' in requestJson and type(requestJson['Rating']) is not int:
        abort(400)
    if 'Director' in requestJson and type(requestJson['Director']) is not str:
        abort(400)
    if 'Votes' in requestJson and type(requestJson['Votes']) is not int:
        abort(400)
    
    if 'Title' in requestJson:
        changeFilm['Title'] = requestJson['Title']
    
    if 'Rating' in requestJson:
        changeFilm['Rating'] = requestJson['Rating']
    
    if 'Director' in requestJson:
        changeFilm['Director'] = requestJson['Director']

    if 'Votes' in requestJson:
        changeFilm['Votes'] = requestJson['Votes']
    
    filmValues = (changeFilm['Title'], changeFilm['Rating'], changeFilm['Director'], changeFilm['Votes'], changeFilm['ID'])
    filmDAO.update(filmValues)
    return jsonify(changeFilm)
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"King Kong\",\"Director\":\"Peter Jackson\",\"Rating\":3}" http://127.0.0.1:5000/films/1

@app.route('/films/<int:id>', methods=['DELETE'])
def deleteFilm(id):
    filmDAO.delete(id)
    return jsonify({"done":True})

@app.route('/votes/<int:id>', methods=['PUT'])
def addVote(id):
    voteAdd = filmDAO.addVote(id)
    if not changeFilm:
        abort(404)
    if not request.json:
        abort(400)
    requestJson = request.json

    if 'Votes' in requestJson and type(requestJson['Votes']) is not int:
        abort(400)

    if 'Votes' in requestJson:
        voteAdd['Votes'] = requestJson['Votes']
    
    voteID = (voteAdded['ID'])
    filmDAO.addVote(voteAdd)
    return jsonify(voteAdd)

@app.route('/votes/leaderboard')
def getLeaderBoard():
    films.sort(key=lambda f: f['Votes'], reverse=True)
    return jsonify(films)

if __name__ == '__main__':
    app.run(debug= True)