# Class methods

class Book:
    def __init__(self, title, author):
    self.title = title
    self.author = author
    
    # It didnt need the class name itself, uses the cls() method
    @classmethod
    def best_book_for_children(cls):
        return cls("Matilda", "Roald Dahl")
    
    
b1 = Book.best_book_for_children() # Can be called on the class
print(b1.title) # Matilda

b2 = Book("Dracula", "Bram Stoker") # Or an instance of the class, this is weird
b3 = b2.best_book_for_children() 
print(b3.title) # Matilda