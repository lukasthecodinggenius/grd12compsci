class Book:
    def read(self):
        print("Reading a book")

class Novel(Book):
    def read(self):
        print("Reading a novel with an exciting plot")

class Textbook(Book):
    def read(self):
        print("Studying a textbook full of information")
        
books = [Novel(), Textbook(), Novel()]

for book in books:
    book.read()
