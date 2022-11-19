
s = "banana"

x = enumerate(s)
print(x)

y = list(x) # list of tupples

print(y)

for index, char in enumerate(s):
    print(char, "has index", index, end=' ')
    
    