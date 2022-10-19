import random

def get_list_from_string(my_list):
    for elmt in my_list:
        print(elmt)

def add_index(numbers):
    """ (list<int> -> list<int>

    """
    
    result = []
    
    for i in range(len(numbers)):
        result.append(numbers[i] + i)
    
    return result


def add_index_change(numbers):
    """ (list<int> -> list<int>

    List can be modified by function
    """
    
    for i in range(len(numbers)):
        numbers[i] += i
    
def find_min(numbers):
    """ (list<int>) -> list<int>
    """
    
    smallest_number = numbers[0]
    for elmt in numbers[1:]:
        if elmt < smallest_number:
            smallest_number = elmt
    return smalles_number


def get_random_numbers(n):
    """ (int) -> list<float>
    Returns a list of n random numbers between 0 and 1
    >>> random.seed(9001)
    >>> get_random_numbers(5)
    """
    random_numbers = []
    
    for i in range(n):
        random_numbers.append(random.random())
    
    return random_numbers
    
def same_length(list1, list2):
    """ (list<str>, list<str>) -> int
    >>> list1 = ["cat", "goat", "house", "puppy"]
    >>> list2 = ["cow", "goat", "house", "puppy"]
    """
    count = 0
    
    for i in range(len(list1)):
        if len(list1[i]) == len(list2[i]):
            count += 1
    
    return count
    
# cannot change the list when inside the loop

# raise ValueError("Primarity is not defined for numbers under 2")
# TypeError, IndexError, Value Error
# raise <some_exception>("message")

def print_multiples(n,m):
    """ (int, int) -> NoneType
    Prints out the frist m multiples of n starting at n.
    Raises a TypeError if the inputs are not interger,
    and raises a ValueError if n < 1 or m < 0.
    
    >>> print_multiples(3, 5)
    3 6 9 12 15 
    """
    
    if n < 1:
        raise ValueError("n needs to be greater or equal to 1")
    
    if m < 0:
        raise ValueError("m needs to be positive")
    
    if type(n) != int or type(m) != int:
        raise TypeError("m and n must be integers")
    
    # include 15
    for x in range(n, n*m+1, n):
        print(x, end=' ')
    
