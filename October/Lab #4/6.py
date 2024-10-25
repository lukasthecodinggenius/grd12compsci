#Class attributes are shared across all instances of a class, whereas instance attributes are unique to each instance.
#For example, in the library class, 'library_name' can be a class attribute that is shared with all books, but 'boot_title' would be instance attribute specific to each book.

class Library:
    library_name = "City Central Library"
    def __init__(self, book_title, author):
        self.book_title = book_title
        self.author = author


book1 = Library("1984", "George Orwell")
book2 = Library("To Kill a Mockingbird", "Harper Lee")

print(Library.library_name)

print(book1.book_title) 
print(book2.book_title)  

Library.library_name = "Downtown Library"

print(book1.library_name) 
print(book2.library_name)  

book1.book_title = "Animal Farm"

print(book1.book_title)
print(book2.book_title)  
