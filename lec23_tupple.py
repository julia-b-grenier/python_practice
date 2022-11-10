"""

• A tuple is an ordered collection of objects, like lists.
• But the number of elements in the tuple, and the values, cannot change after the tuple is created. (A tuple is immutable.)
• We define a tuple using round brackets '()' instead of square brackets '[]'.

"""

# two element tuple
time_tuple = (16, 48)
# making a tuple with just one element
small_tuple = (137, ) # note the comma
# (what would happen without the comma?) it will think that it is a mathematical expression and will give an int
other_tuple = 1, 3, 7
# the parentheses are optional

#• We access specific elements inside a tuple using indices, just like a list or string.
tup = (45, 23, 'abc')
print(tup[1])
#23
#• We can also do negative indexing and slicing.
#• An invalid index will cause an IndexError to be produced.

#• We can convert strings and other data types into tuples using the tuple() function.
t = tuple('lupins')
print(t)
#('l', 'u', 'p', 'i', 'n', 's')

"""
WHY USE TUPPLE AND NOT LIST ?
    • The program is faster when working with tuples.
    • Using tuples ensures that the values in the collection remain constant throughout the program.
    • We can use tuples as keys in a dictionary!

BUILD-IN FUNCTIONS :
    The len(), min(), max(), and sum() built-in functions work the same on tuples as on lists.

"""

# PACKING
#• When we create a string, a list, or a tuple, we are packing several elements into a single object.
s = "cat"
my_list = [5, 'a']
my_tuple = 0, 3, 7

# UNPACKING
#• Unpacking is a useful feature in Python that allow us to
#assign values in a string/list/tuple to multiple variables,
#if we know the exact length of the string/list/tuple.
s = "cat"
a, b, c = s
print(a) # c
print(b) # a
print(c) # t

"""
VALUE ERROR :
When unpacking, the number of variables on the left must
be equal to the number of values in the object on the
right. Otherwise a ValueError is raised.

tup = 1, 2, 3
x, y = tup

ValueError: too many values to unpack
(expected 2)

"""

# Actual tupple unpacking => multiple assignment
city, population, area = 'Montreal', 1704694, 431.5

"""
LOOP USING INDICES
• We can iterate over a list of tuples using a for loop.
• Then we can access each element of the tuple
using indices.
"""
favorite_languages = [('Bob', 'C++'), ('Rahul', 'Python'), ('Yifan', 'R')]
for tup in favorite_languages:
    print(tup[0], tup[1])

"""
LOOP USING UNPACKING
• There's a special syntax for iterating over lists of tuples,
if all tuples in the list have the same size, simplifying our code:
• Each element of the list is a tuple, and at each iteration of
the loop, this tuple is unpacked into the two variables name
and language.
"""
favorite_languages = [('Bob', 'C++'),('Rahul', 'Python'), ('Yifan', 'R')]
for name, language in favorite_languages:
    print(name, language)
    

 



