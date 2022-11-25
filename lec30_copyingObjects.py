import copy

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
b1 = Book("Matilda", "Roald Dahl")
b2 = Book("The BFG", "Roald Dahl")

# Shallow Copy
books = [b1, b2]
b = books

b[0].title = "Dracula"
print(books[0].title) # What prints?

b3 = copy.copy(b1) # still points to the same attributes 
b3.title = "Dracula" # change arrow
print(b1.title) 

books1 = [b1, b2, b3]
books2 = copy.copy(books1)

# Problem when changing attributes that are mutable like lists or dictionary
