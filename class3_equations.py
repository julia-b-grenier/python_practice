

principle_amout = float(input("Enter principal: ")) # correct variable name
r = float(input("Enter r: ")) # not correct variable name
n = int(input("Enter n: "))
number_of_years = int(input("Enter t: "))

A = principle_amout * (1+ r/number_of_years) ** (n * t)

print("A:", round(A, 2)) # Round to 2 decimals

# ** is exponent

# division / always gives float

# floor division // gives integer

# % gives the left over of the division

# if at least one float => answer will be a float

# Follows PEDMAS
