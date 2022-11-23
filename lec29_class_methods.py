# Class methods

class Book:
    def __init__(self, isbn, title, author, genre, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
    
    # It didnt need the class name itself, uses the cls() method
    @classmethod
    def best_book_for_children(cls):
        return cls(0, "Matilda", "Roald Dahl", "", 10.00) # This is a factory methods because it produces object of that class
    
    @classmethod
    def ten_dollar_book(cls, title, author):
        return cls(-1, title, author, "", 10.00)
    
    # Best to make it a instance method and not a static class
    # Could put that in an the bookstore class
    def contained_in(self, booklist):
        for book in books_list:
            if self.isbn == book.isbn:
                return True
        return False
    
    
b1 = Book.best_book_for_children() # Can be called on the class
print(b1.title) # Matilda

b2 = Book.ten_dollar_book("Dracula", "Bram Stoker") # Or an instance of the class, this is weird
b3 = b2.best_book_for_children() 
print(b3.title) # Matilda