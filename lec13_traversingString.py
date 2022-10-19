#Traversal using a while loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter, end=" ")
    index = index + 1

print("\n")

#Looping by index
s = "artichockes"
for i in range(len(s)):
    print(s[i], end=" ")
    
print("\n")

#Looping by value
fruit = "watermelon"    
for letter in fruit:
    print(letter, end=" ")