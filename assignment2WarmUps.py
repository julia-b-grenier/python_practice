def swap(x,y):
    """ (int,int) -> NoneType
    1. Print the value of x and y
    2. Swap the values of the variables x and y, so that whatever was in x is now in y and whatever was
    in y is now in x
    3. Print the value of x and y again.
    
    >>> swap(3, 4)
    inside swap: x is:3 y is:4
    inside swap: x is:4 y is:3
    """
    print("inside swap: " + "x is:" + str(x) + " y is:" + str(y))
    x, y = y, x
    print("inside swap: " + "x is:" + str(x) + " y is:" + str(y))    

def replace_all(word, char1, char2):
    if len(char1) != 1 or len(char2) != 1 :
        print("ValueError")
    else:
        new_word = ""
        for char in word:
            if (char == char1):
                char = char2
            new_word = new_word + char
            
        print(new_word)
        
lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     
        
def make_lower(word):
    new_word = ""
    for char in word:
        if (upper_alpha.find(char) != -1):
            char = lower_alpha[upper_alpha.find(char)]
        new_word = new_word + char
    print(new_word)
    