# class Book:
#     def __init__(self,title,author,is_checked_out = False):
#         self.title = title
#         self.author = author
#         self._is_checked_out = is_checked_out

#     def get_is_checked_out(self):
#         return self._is_checked_out
    
#     def set_is_checked_out(self):
#         self._is_checked_out = True

# class Library:
#     def __init__(self,_books):
#         self.__books =[]
#         pass   

  

#     def add_book(self,book):
#         if isinstance(book,Book):
#             self.__books.append(book)
#             return book
        
#     def check_out_book(self,title):
#         self.title = title
#         for book in self.__books:
#             if not book.get_is_checked_out():
#                 book.set_is_checked(True) 
#                 return self.title
            
#     def return_book(self,title):
#         self.title = title

#         for book in self.__books:
#             if book.title == title:
#                 if book.get_checked_out():
#                     book.set_is_checked_out(False)
#                     return book.title
            
#     def list_available_books(self):
#         for book in self.__books:
#             print(book)
class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out  

    def get_is_checked_out(self):
        """Return True if the book is checked out, False otherwise."""
        return self._is_checked_out
    
    def set_is_checked_out(self, status):
        """Set the checked-out status of the book."""
        self._is_checked_out = status

    def __str__(self):
        status = "Checked out" if self._is_checked_out else "Available"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        """Add a Book object to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' by {book.author}.")
        else:
            print("Error: Only Book objects can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.get_is_checked_out():
                    book.set_is_checked_out(True)
                    print(f"You checked out '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.get_is_checked_out():
                    book.set_is_checked_out(False)
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.get_is_checked_out()]
        if not available_books:
            print("No books available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")



            
    



            




                



        
        





    
