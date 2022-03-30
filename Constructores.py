class Libro:
    def __init__(self,isbn,author,title,edition,year,no_copies,no_available_copies,no_bookshelf,no_bookshelf_row):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.edition = edition
        self.year = year
        self.no_copies = no_copies
        self.no_available_copies = no_available_copies
        self.no_bookshelf = no_bookshelf
        self.no_bookshelf_row = no_bookshelf_row

class Prestamista:
    def __init__(self,cui,last_name,first_name):
        self.cui = cui
        self.last_name = last_name
        self.first_name = first_name

class Prestamo:
    def __init__(self,cui,isbn):
        self.cui = cui
        self.isbn = isbn