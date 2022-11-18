import doctest

def sum_at_even_indices(numbers):
    """ (list<int>) -> int
    Returns the sum of the elements at even indices
    of the list numbers.
    
    >>> sum_at_even_indices([2,7,9,1])
    11
    """
    
    count = 0
    
    """
    for i in range(len(numbers)):
        if i % 2:
            count += numbers[i]
    """
         
    # Using enumerate
    for i,number in enumerate(numbers):
        if i % 2 == 0:
            count += number


if __name__ == "__main":
    doctest.testmod()