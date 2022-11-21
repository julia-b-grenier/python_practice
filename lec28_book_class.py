import doctest

class Book:
    """ A class to represent a book.

    Instance attributes:
    * ISBN: int
    * title: str
    * author: str
    * genre: str
    * price: float
    """
    
    def __init__(self, isbn, title, author, genre, price):
        """ (int, str, str, str, float) -> Book/NoneType
        Creates an object of type Book.
        
        >>> s = Book("152", "Sora & Haena", "Unknown", "Yuri", 12.99)
        >>> s.title
        'Sora & Haena'
        >>> s.price
        12.99
        """
        
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        
    def __str__(self):
        """ () -> str
        Returns as a string the title and price of the book.
        
        >>> s = Book("152", "Sora & Haena", "Unknown", "Yuri", 12.99)
        >>> str(s)
        'Sora & Haena @ $12.99'
        """
        
        return self.title + " @ $" + str(self.price)
    
    
    def on_sale(self):
        """ () -> NoneType
        Cuts the price of the book in two.
        
        >>> s = Book("152", "Sora & Haena", "Unknown", "Yuri", 12.99)
        >>> s.on_sale()
        >>> str(s)
        'Sora & Haena @ $6.5'
        """
        self.price = round(self.price/2, 2)
        
    def is_cheaper(self, other_book):
        """ (Book) -> bool
        Returns True if the current book is cheaper
        
        >>> s = Book("152", "Sora & Haena", "Unknown", "Yuri", 12.99)
        >>> a = Book("152", "Other Book", "Unknown", "Yuri", 2.50)
        >>> s.is_cheaper(a)
        False
        """
        
        return self.price < other_book.price


def display_books(l_books):
    """ (list<Book>) -> NoneType
    """
    for book in l_books:
        print(book)
        


def start_sale(l_books):
    """ (list<Book>) -> NoneType
    """
    for book in l_books:
        book.on_sale()
        
        
        
if __name__ == "__main__":
    doctest.testmod()
    
    
    s = Book("152", "Sora & Haena", "Unknown", "Yuri", 12.99)
    a = Book("152", "Other Book", "Unknown", "Yuri", 2.50)