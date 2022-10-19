#logical operators

# not
print(not 5==5) #False

# and (both side needs to be True to return True)
print(5 == 5 and True) #True
print(5 == 5 and False) #False

# or (at least one needs to be True)
print(False or True) #True

# Order : not, and, or
# if ties : left to right

b = True
a = True

print(b and not a or b)

# Error True == not False
# True == (not False)

print(False or 1 // 2.0 < 3.5)



