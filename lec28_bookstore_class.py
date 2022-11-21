class Bookstore:
    def __init__(self, name, books_list):
        self.name = name
        
        self.book_dict = {}
        for books in book_list:
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
                
