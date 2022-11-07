import doctest

def all_positive(width, height, depth):
    """ (int, int, int) -> bool
    Returns True if the numbers received are all positive. Useful to make sure the width,
    the height and the depth are valid numbers before doing invalid mathematic operations like
    a division by 0.
    
    >>> all_positive(2, 3, 1)
    True
    
    >>> all_positive(2, 0, 1)
    False
    
    >>> all_positive(2, 0, 0)
    False
    
    """
    numbers_all_positive = True
    if (width < 1 or height < 1 or depth < 1):
        numbers_all_positive = False
        
    return numbers_all_positive


doctest.testmod()