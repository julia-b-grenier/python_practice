# Julia B.Grenier

# import statement
import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

pythagore = math.sqrt(pow(a, 2) + pow(b,2))
print("C is:", pythagore)


print(abs(-15)) # absolute value

print(pow(8, 2)) # power

print(round(52.25)) # rounding

print(math.sin(90)) # requires importing the math module
print(math.sqrt(4))
print(math.radians(90))
print(math.fabs(-15.515))

# help(math) gives the complete documentation

# single = assignment operator
# double == equality operator

print(True) # With a capital T
print(False) # With a capital F

print("cat" < "dog") # gives True because c comes before d in the alphabets

# Better way ti test if two floats are equal is to check whether they are close enough to one another

sum1 = 1.1 + 2.2
epsilon = 0.0001
print(abs(sum1 - 3.3) < epsilon) # outputs True

