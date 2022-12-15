import copy
class Author:
    def __init__(self, name):
        self.name = name
        
me = Author("Disgruntled Bovine")
you = Author("Disgruntled Bovine")

print(me, you)
if me == you:
    print("Imposter!")
    
other = copy.copy(me)
print(other)
if other == me or other == you:
    print("I am Spartacus.")