x = [5,6,7]

y = x # aliais o

"""
Because x and y are different names for the same thing,
they are sometimes called aliases.

If you actually want to copy the list, not just a reference,
you need to create a new list.
"""

y[0] += 1

print(x[0], y[0]) # both print 6


def example(a): # behave the same as def example(j) 
    
    a[0] = a[0] * 5 # no need to return because lists are mutable


a = [5,6,7]

example(a)

print(a[0])

