class Libro:
    def __init__(self,isbn,author,title,year,no_copies,no_available_copies):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.year = year
        self.no_copies = no_copies
        self.no_available_copies = no_available_copies
    

class Prestamista:
    def __init__(self,cui,last_name,first_name,status = False):
        self.cui = cui
        self.last_name = last_name
        self.first_name = first_name
        self.status = status

class Prestamo:
    def __init__(self,uuid,cui,isbn,lenDate,returnDate = 'Pendiente'):
        self.uuid = uuid
        self.cui = cui
        self.isbn = isbn
        self.lenDate = lenDate
        self.returnDate = returnDate