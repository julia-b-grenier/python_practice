import matplotlib.pyplot as plt

from lec28_book_class import *

class Bookstore:
    def __init__(self, name, books_list):
        self.name = name
        
        self.books_dict = {}
        for book in books_list:
            self.books_dict[book.ISBN] = book
            
            
    def display_books(self):
        """ (list<Book>) -> NoneType
        """
        for book in self.books_dict.values():
            print(book)
            

    def start_sale(self):
        """ (list<Book>) -> NoneType
        """
        for book in self.books_dict.values():
            book.on_sale()
            
    def plot_by_genre(self):
        
        genres = {}
        for book in self.books_dict.values():
            if book.genre not in genres:
                genres[book.genre] = 1
            else:
                genres[book.genre] += 1
        
        print(genres)
        
        plt.title(self.name + " - Books by genre")
        plt.ylabel("Number of Books")
        plt.xlabel("Genres")
        plt.bar(genres.keys(),genres.values())
        plt.show()
        
    
    def books_by_genre(self, genre):
        """ (str) -> list<Book>
        Returns a list of books in the bookstrore
        that have the specific genre.
        
        >>> 
        
        """
        
        genre_books = []
        
        for book in self.books.value():
            if book.genre == genre:
                genre_books.append(book)
        
        return genre_books
    
    def get_all_genres():
        genres = []
        for book in self.books_dict.values():
            if book.genre not in genres:
                genres.append(book.genre)
        return genres
    
    def find_cheapest(self, genre):
        genre_books = self.books_by_genre(genre)
        
        cheapest_book = genre_books[0]
        
        for book in genre_books:
            if book.ischeaper(cheapest_book):
            #if book.price < cheapest_book.price:
                cheapest_book = book
                
        return cheapest_book
            
                
        
def create_bookstore(name, list_info_books):
    """ (str, list<str>) -> Bookstore
    The function takes
    as input a string indicating the name of the bookstore, and a list of strings each containing information
    about a book. The data related to a book is separated by tabs. The function should create a list of
    objects of type Book and then uses this list and the name to create and return a Bookstore object.
    
    >>> julia_bookstore = create_bookstore("Julia",["152151\tThe Little Prince\tAntoine\tChildren\t14.85","289065\tFrankenstein\tMary Shelley\tScience fiction\t20.85"])
    
    """
    
    l_books = []
    
    for info_book in list_info_books:
        l_infos = info_book.split("\t")
        isbn, title, author, genre, price = l_infos
        l_books.append(Book(int(isbn),title,author,genre,float(price)))
        
    return Bookstore(name, l_books)

def create_bookstore_from_file(filename):
    """ (str) -> Bookstore
    The function takes as input a
    filename containing information about all the books in this bookstore. Reading the file line by line, the
    function creates a list of objects of type Book. It then uses this list and the name of the file (without its
    extension) to create and return a bookstore.

    """
    
    name = filename[:filename.find(".")]
    
    fobj = open(filename, "r")
    content = fobj.read().strip().split("\n")
    fobj.close()
    
    return create_bookstore(name,content)
