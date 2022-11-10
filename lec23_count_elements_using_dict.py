import doctest

def count_elements(input_list):
    """ (list<str>) -> dict<str, int>
    Returns a dictionary of the number of occurrences
    of each string in my_list.
    
    >>> count_elements(["apple", "banana", "apple"])
    {'apple': 2, 'banana': 1}
    """
    
    def count_occurrences(input_list):
     count = {} # create an empty dictionary
     # iterate through the elements in the list
     for element in input_list:
         if element in count:
             # there's already an item with element as key
             count[element] += 1 # increment
         else:
             # we see element for the first time
             count[element] = 1 # initialize the item with value 1
     return count
    

def count_capitals(my_list):
    """ (list<str>) -> dict<str, int>
    Write a function that takes as input a list of strings and
    counts how many words start with each of the upper case
    letters of the English alphabet (A-Z). Do so using a
    dictionary.
    
    >>> count_capitals(["Apple", "Banana", "Apple"])
    {'A': 2, 'B': 1}
    
    """
    def count_occurrences(input_list):
        first_letters = []
     
        for element in input_list:
            if elmt[0].isupper():
                first_letter.append(elmt[0])

        return count_elements(first_letters)


    

if __name__ == "main":
    doctest.testmod()