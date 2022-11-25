# to modify the behavior of == we can define the method __eq__ inside our class.

# if == is not define, act as 'is' and compare the id

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __eq__(self, other): # Operator overwriting
        return self.title == other.title
    
    def __lt__(self, other):
        return self.price < other.title

"""

We can override many kinds of default operators by
defining our own methods:
    • __lt__: less than operator "<"
    • __gt__: greater than operator ">"
    • __le__/__ge__: less than or equal to '<=', greater than or equal to '>='
    • __eq__/__ne__: equal to '==', not equal to '!='

See here for a complete list:
https://docs.python.org/3/reference/datamodel.html#specialnames


"""