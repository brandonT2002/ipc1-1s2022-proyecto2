from Constructores import Libro,Prestamista, Prestamo
from datetime import datetime
import json
import random
class Controlador:
    def __init__(self):
        self.libros = []
        self.prestamistas = []
        self.prestamos = []

        #self.createBook(1,'Brandon','Java',1999,2,2)
        #self.createBook(2,'Brandon','Java',2000,2,2)
        #self.createBook(3,'Brandon','Java',2001,2,2)
        #self.createBook(4,'Brandon','Python',2000,3,3)
        #self.createBook(5,'Brandon','Python',2002,3,3)
        #self.createBook(6,'Brandon','C#',2005,3,3)
        #self.createBook(7,'Brandon','C#',2006,3,3)
        #self.createBook(8,'Brandon','C#',2008,3,3)
        #self.createBook(9,'Jefferson','Go',2015,5,5)
        #self.createBook(10,'Andy','Go',2016,5,5)
        #self.createBook(11,'Brandon','Unity',2019,5,5)
        #self.createBook(12,'Brandon','Unreal Engine',2022,5,5)
        #self.createCustomer('1','Tejaxun','Jefferson')
        #self.createCustomer('2','Gates','Bill')
        #self.createCustomer('3','Jobs','Steve')
        #self.createCustomer('4','>uckerberg','Mark')
        #self.newLoan('1',1)
        #self.returnBook(self.prestamos[0].uuid)
        #self.newLoan('1',2)
        #self.returnBook(self.prestamos[1].uuid)
        #self.newLoan('1',3)
        #self.returnBook(self.prestamos[2].uuid)
        #self.newLoan('4',4)
        #self.returnBook(self.prestamos[3].uuid)

    # UUID
    def generateUuid(self):
        upperLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        lowerLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        numbers = ['1', '2', '3', '4', '5', '6', '7','8','9','0']

        characters = upperLetters + lowerLetters + numbers
        uuid = []

        for i in range(5):
            randomRharacter = random.choice(characters)
            uuid.append(randomRharacter)

        uuid = "".join(uuid)
        return uuid

    # Books
    def createBook(self,isbn,author,title,year,noCop,noCopDisp):
        if self.verify(isbn):
            return '{"msg":"El libro ya existe"}',400
        self.libros.append(Libro(isbn,author,title,year,noCop,noCopDisp))
        return '{"msg":"Libro creado exitosamente"}',200

    def updateBook(self,isbn,author,title,year):
        book = self.verify(isbn)
        if book:
            book.author = author
            book.title = title
            book.year = year
            return '{"msg":"Libro actualizado"}',200
        return '{"msg":"Libro no encontrado"}',400

    def searchBooks(self,dict):
        self.search_books = [book for book in self.libros]
        if not self.verifyDict(dict,'title') and not self.verifyDict(dict,'year_from') and not self.verifyDict(dict,'year_to') and not self.verifyDict(dict,'author'):
            return json.dumps([book.__dict__ for book in self.search_books])
        if self.verifyDict(dict,'title'):
            self.search_books = [book for book in self.search_books if book.title == dict['title']]
        if self.verifyDict(dict,'year_from'):
            self.search_books = [book for book in self.search_books if book.year >= dict['year_from']]
        if self.verifyDict(dict,'year_to'):
            self.search_books = [book for book in self.search_books if book.year <= dict['year_to']]
        if self.verifyDict(dict,'author'):
            self.search_books = [book for book in self.search_books if book.author >= dict['author']]
        return json.dumps([book.__dict__ for book in self.search_books])

    # Prestamistas

    def createCustomer(self,cui,last_name,first_name):
        customer = self.verifyC(cui)
        if customer:
            return '{"smg":"El prestamista ya existe"}',400
        self.prestamistas.append(Prestamista(cui,last_name,first_name))
        return '{"msg":"Prestamista creado exitosamente"}',200

    def getCustomer(self,cui):
        customer = self.verifyC(cui)
        if not customer:
            return '{"msg":"Prestamista no encontrado"}',400
        record = self.getRecord(cui)
        return json.dumps({"cui":customer.cui,"first_name":customer.first_name,"last_name":customer.last_name,"record":record}),200

    def newLoan(self,cui,isbn):
        customer = self.verifyC(cui)
        book = self.verify(isbn)
        lenDate = datetime.today().strftime('%y-%m-%d %H:%M')
        status = self.checkPendingB(cui)
        if customer and book:
            if status:
                while True:
                    uuid = self.generateUuid()
                    if not self.verifyUuid(uuid):
                        if self.changeNumberB(book.isbn,-1):
                            self.prestamos.append(Prestamo(uuid,cui,isbn,lenDate))
                            customer.status = True
                            return '{"uuid":"' + uuid +'"}',200
                        else:
                            return '{"msg":"No hay libros disponibles"}',200
            return '{"msg":"Prestamo pendiente"}'
        return '{"smg":"No se ha podido realizar el prestamo"}',400

    def returnBook(self,uuid):
        id = self.verifyUuid(uuid)
        if id:
            status = self.checkPendingB(id.cui)
            if not status:
                customer = self.verifyC(id.cui)
                self.changeNumberB(id.isbn,1)
                id.returnDate = datetime.today().strftime('%y-%m-%d %H:%M')
                customer.status = False
                return '{"msg":"Libro devuelto exitosamente"}',200
            return '{"msg":"Préstamo Concluido"}',200
        return '{"msg":"El prestamo no existe"}'    

    def changeNumberB(self,isbn,n):
        for i in range(len(self.libros)):
            if self.libros[i].isbn == isbn and self.libros[i].no_available_copies > 0:
                self.libros[i].no_available_copies += n
                return True
        return False

    def getRecord(self,cui):
        record = []
        for i in self.prestamos:
            if i.cui == cui:
                record.append({"uuid":i.uuid,"isbn":i.isbn,"title":self.getTitle(i.isbn),"lenDate":i.lenDate,"returnDate":i.returnDate})
        return record
    
    def getTitle(self,isbn):
        for i in self.libros:
            if i.isbn == isbn:
                return i.title

#Validaciones

    def verify(self,isbn) -> Libro:
        for i in self.libros:
            if i.isbn == isbn:
                return i
        return None

    def verifyTitle(self,title) -> Libro:
        for i in self.libros:
            if i.title == title:
                return i
        return None
    
    def verifyC(self,cui) -> Prestamista:
        for i in self.prestamistas:
            if i.cui == cui:
                return i
        return None

    def verifyUuid(self,uuid) -> Prestamo:
        for i in self.prestamos:
            if i.uuid == uuid:
                return i
        return None

    def checkPendingB(self,cui) -> Prestamista:
        for i in self.prestamistas:
            if i.cui == cui and not i.status:
                return i
        return None

    def verifyDict(self,dict,key):
        for k in dict:
            if k == key:
                return True
        return False