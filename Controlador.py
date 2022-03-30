from flask import jsonify, request
from Constructores import Libro

class Controlador:
    def __init__(self):
        self.libros = []
        self.prestamistas = []
        self.prestamos = []

    def createBook(self,isbn,autor,title,edition,year,noCop,noCopDisp,estante,nFila):
        if self.verify(isbn):
            return '{"msg":"Libro ya existe"}'
        self.libros.append(Libro(isbn,autor,title,edition,year,noCop,noCopDisp,estante,nFila))
        return '{"msg":"Libro creado exitosamente"}'
    
    def verify(self,isbn):
        for i in self.libros:
            if i.isbn == isbn:
                return True
        return False