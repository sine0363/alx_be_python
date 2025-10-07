class Book:
    def __init__(self,title,author,is_checked_out = False):
        self.title = title
        self.author = author
        self.__is_checked_out = is_checked_out

    def get_is_checked_out(self):
        return self.__is_checked_out
    
    def set_is_checked_out(self):
        self.__is_checked_out = True

class Library:
    def __init__(self,_books):
        self.__books =[]
        pass   

  

    def add_book(self,book):
        if isinstance(book,Book):
            self.__books.append(book)
            return book
        
    def check_out_book(self,title):
        self.title = title
        for book in self.__books:
            if not book.get_is_checked_out():
                book.set_is_checked(True) 
                return self.title
            
    def return_book(self,title):
        self.title = title

        for book in self.__books:
            if book.get_checked_out():
                book.set_is_checked_out(False)
                return book.title
            
    def list_available_books(self):
        for book in self.__books:
            print(book)


            
    



            




                



        
        





    
