import copy

# deep copy
# takes a long time

b1 = Book("Matilda", "Roald Dahl")
b2 = Book("The BFG", "Roald Dahl")

books = [b1, b2]
b = copy.deepcopy(books)
b[0].title = "Dracula"

print(books[0].title) # prints Matilda