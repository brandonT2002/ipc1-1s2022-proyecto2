from flask import Flask, jsonify, request
from Controlador import Controlador

app = Flask(__name__)

ctrl = Controlador()

@app.route('/')
def ping():
    return jsonify({'message':'pong!'})


@app.route('/book', methods = ['POST'])
def createBook():
    data = request.json
    return ctrl.createBook(
        data['isbn'],
        data['author'],
        data['title'],
        data['edition'],
        data['year'],
        data['no_copies'],
        data['no_available_copies'],
        data['no_bookshelf'],
        data['no_bookshelf_row']
        )


if __name__ == '__main__':
    app.run(debug = True, port = 4000)