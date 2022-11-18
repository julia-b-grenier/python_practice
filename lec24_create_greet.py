def create_greet(message):
    def greet(name):
        print(message + " " + name + "!")
    return greet

my_greet = create_greet("Welcome back")

my_greet("Julia")

my_greet = create_greet("Hello")

my_greet("Hello")