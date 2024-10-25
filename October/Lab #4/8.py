class Book:
    def read(self):
        print("Reading a book")

class Novel(Book):
    def read(self):
        print("Reading a novel")

class Textbook(Book):
    def read(self):
        print("Studying a textbook")
        
books = [Novel(), Textbook(), Novel()]

for book in books:
    book.read()
