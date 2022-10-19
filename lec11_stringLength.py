
s = "A string"
print(len(s))

# each character has an index that indicates its position in the string
# starts by index 1

fruit = "banana"
print(fruit[0])
print(fruit[-1]) # when we go backward we start at -1

#valid range for indices of a string s is
print(s[-len(s)], s[len(s)-1])

a = "Monty Python"
print(a[6:])
print(a[:5])
print(a[2:5])

# get every second character between index 0 to 5
print(a[0:5:2])

hello = "Hello World"
#reverse string
print(hello[::-1])

# in python strings are immutable objects, we cannot use the square brackets to modify a character in the string

new_hello = "|-|" + hello[1:]
print(new_hello)


example = "for example"
t = example
example = example[4:]
print(example)
print(t)


print(hello.lower()) #returns a new string with all lower case letters
print(hello.upper()) #returns a new string with all upper case letters

