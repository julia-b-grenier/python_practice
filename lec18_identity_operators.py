"""

in the shell

>>> x = 500
>>> y = 500
>>> z = x
>>> x is y
False
>>> x is z
True

"""

# Python optimize
#in the shell you'll see False displayed.
#If you run the module, all print statements will display True

x = 500
y = 500
print(id(x) == id(y))
f = 5.5
g = 5.5
print(id(f) == id(g))
s = "Every time I learn something new, it pushes \
some old stuff out of my brain. - Homer"
t = "Every time I learn something new, it pushes \
some old stuff out of my brain. - Homer"
print(id(s) == id(t))

