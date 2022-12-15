import random

class FunaDansu:
    
    def __init__(self, dims):
        self.dims = dims
        self.data = None
        self.num_compartments = dims[0] * dims[1] * dims[2]
        
    def stow_away(self, data):
        if len(data) > self.num_compartments:
            raise ValueError
        
        self.data = data
        
    def rock_the_boat(self):
        try: 
            random.shuffle(self.data)
        except TypeError:
            print("it has no effect")
            