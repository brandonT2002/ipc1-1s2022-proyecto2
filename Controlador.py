from itsdangerous import json
from Constructores import Libro
import json
class Controlador:
    def __init__(self):
        self.libros = []
        self.prestamistas = []
        self.prestamos = []

    def createBook(self,isbn,autor,title,edition,year,noCop,noCopDisp,estante,nFila):
        if self.verify(isbn):
            return '{"msg":"El libro ya existe"}'
        self.libros.append(Libro(isbn,autor,title,edition,year,noCop,noCopDisp,estante,nFila))
        return '{"msg":"Libro creado exitosamente"}'
    
    def getBook(self,isbn):
        libro = self.verify(isbn)
        if not libro:
            return '{"msg":"Libro no encontrado"}'
        return json.dumps(libro.__dict__)

    def verify(self,isbn):
        for i in self.libros:
            if i.isbn == isbn:
                return i
        return None