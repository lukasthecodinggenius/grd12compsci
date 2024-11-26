class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.isAvailable = True  # Books are available by default when added.


class LibraryManager:
    def __init__(self):
        self.books = []  # Store books in a list/one dimensional arraw.
        self.borrower_records = []  # Track borrowing records with a two dimensional array.

    def add_book(self, title, author, ISBN):
    
        #Adds a new book to the library if the ISBN is valid.
        if len(ISBN) == 13 and ISBN.isdigit():  # ISBN must be a 13-digit number in order to be valid.
            self.books.append(Book(title, author, ISBN))  # Add the new book to the list.
            print(f"Book '{title}' added successfully.")
        else:
            print("Invalid ISBN. Must be a 13-digit number.")

    def remove_book(self, ISBN):
        #Removes a book from the library using its ISBN.
        for book in self.books:
            if book.ISBN == ISBN:  # Check if the book exists in the collection.
                self.books.remove(book)  # Remove the book from the list.
                print(f"Book '{book.title}' removed successfully.")
                return
        print("Book not found.")  # ISBN does not match any book.

    def list_books(self, sort_by=None):
        # Sort books based on the specified attribute.
        if sort_by == "title":
            sorted_books = sorted(self.books, key=lambda b: b.title)
        elif sort_by == "author":
            sorted_books = sorted(self.books, key=lambda b: b.author)
        else:
            sorted_books = self.books
        print("Books in the Library:")
        for book in sorted_books:
            status = "Available" if book.isAvailable else "Borrowed"
            print(f"{book.title} by {book.author} (ISBN: {book.ISBN}) - {status}")

    def borrow_book(self, borrower_id, book_ISBN):
        for book in self.books:
            if book.ISBN == book_ISBN:  # Find the book with the matching ISBN.
                if book.isAvailable:  # Check if the book is available for borrowing.
                    book.isAvailable = False  # Mark the book as borrowed.
                    # Record the borrower details: ID, book ISBN, and borrow date (as "YYYY-MM-DD").
                    borrow_date = "2024-11-26"  # Fixed date for simplicity.
                    self.borrower_records.append([borrower_id, book_ISBN, borrow_date, "Pending"])
                    print(f"Book '{book.title}' borrowed by Borrower ID {borrower_id}.")
                    return
                else:
                    print("Book is already borrowed.")  # Book is not available.
                    return
        print("Book not found.")  # ISBN does not match any book.

    def return_book(self, borrower_id, book_ISBN):
        for record in self.borrower_records:
            # Check for a matching borrower record where the book is still pending return.
            if record[0] == borrower_id and record[1] == book_ISBN and record[3] == "Pending":
                record[3] = "2024-11-26"  # Fixed return date for simplicity.
                for book in self.books:
                    if book.ISBN == book_ISBN:  # Find the corresponding book.
                        book.isAvailable = True  # Mark the book as available.
                        print(f"Book '{book.title}' returned by Borrower ID {borrower_id}.")
                        return
        print("No matching borrow record found.")  # Borrower or book not found.

    def calculate_late_fee(self, borrower_id, book_ISBN):
        for record in self.borrower_records:
            if record[0] == borrower_id and record[1] == book_ISBN:
                borrow_date = record[2]  # Borrow date as "YYYY-MM-DD".
                # For simplicity, assume borrow_date and return_date are integers (day of month).
                borrow_day = int(borrow_date.split("-")[2])  # Extract the day part.
                if record[3] == "Pending":
                    return_day = 26  # Assume today's day is 26 for pending returns.
                else:
                    return_day = int(record[3].split("-")[2])  # Extract the day part from return date.

                days_borrowed = return_day - borrow_day
                overdue_days = max(0, days_borrowed - 14)  # Subtract the allowed 14 days.
                late_fee = overdue_days * 1  # $1 per day late.
                print(f"Late fee for Borrower ID {borrower_id}: ${late_fee:.2f}.")
                return late_fee
        print("No matching record for fee calculation.")  # No record found.
        return 0


# Example Output
library = LibraryManager()
library.add_book("The Road", "Cormac McCarthy", "1234567890123")
library.add_book("Psycho", "Robert Bloch", "9876543210123")

library.list_books(sort_by="title")

library.borrow_book("B001", "1234567890123")
library.list_books()

library.calculate_late_fee("B001", "1234567890123")

library.return_book("B001", "1234567890123")
library.list_books()
