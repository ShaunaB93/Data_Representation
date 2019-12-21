from flask import Flask
from flask import jsonify

app = Flask(__name__, static_url_path='', static_folder='.')

films=[{
    "ID":1,
    "Title":"Harry Potter",
    "Rating":10,
    "Director":"David Yates"
},
{
    "ID":2,
    "Title":"The Avengers",
    "Rating":9,
    "Director":"Joss Whedon"
},
{
    "ID":3,
    "Title":"Superman Returns",
    "Rating":5,
    "Director":"Bryan Singer"
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
        return jsonify({}), 204
    
    return jsonify(filmCheck[0])

@app.route('/films', methods=['POST'])
def createFilm():
    return "in create film"

@app.route('/films/<int:id>', methods=['PUT'])
def updateFilm(id):
    return "in update for id " +str(id)

@app.route('/films/<int:id>', methods=['DELETE'])
def deleteFilm(id):
    return "in delete for id " +str(id)

if __name__ == '__main__':
    app.run(debug= True)