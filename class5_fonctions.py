# void functions and fruitful functions

name = input("Enter your name: ")

def greetings(n):
    print("Hello", n)
    
def twogreetings(n):
    greetings(n)
    greetings(n)
    
twogreetings(name)