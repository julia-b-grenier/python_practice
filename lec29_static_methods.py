# Static methods

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # All code related to book is inside the same code
    @staticmethod
    def same_author(books):
        a = books[0].author
        for b in books:
            if b.author != a:
                return False
        return True
    
b1 = Book("Matilda", "Roald Dahl")
b2 = Book("The BFG", "Roald Dahl")
books = [b1, b2]
print(Book.same_author(books)) # True

l = [b1, b2]
l2 = [b2, b2]
l2 = l + l2
print(l2)
