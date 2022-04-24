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
        data['year'],
        data['no_copies'],
        data['no_available_copies']
        )

@app.route('/book', methods = ['PUT'])
def updateBook():
    data = request.json
    return ctrl.updateBook(
        data['isbn'],
        data['author'],
        data['title'],
        data['year']
    )

@app.route('/book', methods = ['GET'])
def searchBooks():
    data = request.json
    return ctrl.searchBooks(
        data
    )

@app.route('/person', methods = ['POST'])
def createCustomer():
    data = request.json
    return ctrl.createCustomer(
        data['cui'],
        data['last_name'],
        data['first_name']
        )

@app.route('/person/:cui', methods = ['GET'])
def getCustomer():
    data = request.json
    return ctrl.getCustomer(
        data['cui']
        )

@app.route('/borrow', methods = ['POST'])
def newLoan():
    data = request.json
    return ctrl.newLoan(
        data['cui'],
        data['isbn']
    )

@app.route('/borrow/:uuid', methods = ['PATCH'])
def returnBook():
    data = request.json
    return ctrl.returnBook(
        data['uuid']
    )


if __name__ == '__main__':
    app.run(debug = True, port = 4000)