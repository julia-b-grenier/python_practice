#from math import sin,radians # no need to write math.sin() each time



# n is the loop counter
n = 3
while n > 0:
    print("Value of n is :", n)
    n -= 1

# iteration is a single execution of the instructions in the body of the loop
# repeat the nody as long as the condition evaluates to True

i = 0
while i < 100:
    if i % 5 == 0:
        print(i)
    i += 1