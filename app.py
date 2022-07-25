from flask import Flask, jsonify, request
from flask_cors import CORS
from Controlador import Controlador

app = Flask(__name__)
CORS(app)
ctrl = Controlador()

@app.route('/')
def ping():
    return jsonify({'message':'API Biblioteca'})


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
    try:
        data = request.json
    except:
        data = '{}'
    return ctrl.searchBooks(
        data
    )

@app.route('/record/<cui>', methods = ['GET'])
def getRecord(cui):
    return ctrl.getRecordCui(cui)

@app.route('/person', methods = ['POST'])
def createCustomer():
    data = request.json
    print(data)
    return ctrl.createCustomer(
        data['cui'],
        data['last_name'],
        data['first_name']
        )

@app.route('/person', methods = ['GET'])
def getCustomer():
    return ctrl.getCustomer()

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

@app.route('/book', methods = ['DELETE'])
def deleteBooks():
    data = request.json
    return ctrl.deleteBooks(
        data['isbn']
        )

@app.route('/person', methods = ['DELETE'])
def deleteCustomer():
    data = request.json
    return ctrl.deleteCustomer(
        data['cui']
    )

if __name__ == '__main__':
    app.run(debug = True, port = 4000)