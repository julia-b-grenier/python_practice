
class Cat:
    
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
    def meow(self):
        if self.age < 1:
            print(self.name, "mews")
        else:
            print(self.name, "meows")
            
    def birthday(self):
        self.age += 1