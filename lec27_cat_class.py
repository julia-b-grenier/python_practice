import datetime

class Cat:
    Created_cat = 0
    
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
        Cat.Created_cat += 1
        
    def __str__(self):
        return self.name + " is " + str(self.age)
    
    # instance method or static but ~ reads less good
    def is_older_than(self, other):
        return self.age > other.age
    
    # makes more sense to be a static method
    def find_oldest(cats_list):
        oldest = cats_list[0]
        oldest_index = 0
        for index, cat in enumerate(cats_list[1:]):
            if cat.is_older_tan(oldest):
                oldest = cat
                oldest_index = index + 1
        return oldest_index
    
    @classmethod
    def from_birthday(cls, name, birthdate):
        cur_date = datetime.date.today()
        difference = cur_date - birthdate
        diff_days = difference.days
        age = diff_days//365
        
        return cls(name, age)

        
    def meow(self):
        if self.age < 1:
            print(self.name, "mews")
        else:
            print(self.name, "meows")
            
    def birthday(self):
        self.age += 1
        
