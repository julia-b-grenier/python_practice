import doctest


def avg(x):
    return sum(x) / len(x)

def get_indices(l,f):
    """ (list<int>, function()) -> list<int>
    Calls the given function with the given list as input to abtain a value V
    and returns a list of indices that correspond to the elements in the list that
    are equal to V
    
    >>> get_indices([5,2,4,8,9,10], max)
    [5]
    
    >>> get_indices([5,2,2,3], avg)
    [3]
    
    >>> get_indices([5,2,2,3], min)
    [1, 2]
    
    """
    result = f(l)
    
    indices = []
    
    for index, numbers in enumerate(l):
        if numbers == result:
            indices.append(index)
            
    return indices
    
if __name__ == "__main__":
    doctest.testmod()