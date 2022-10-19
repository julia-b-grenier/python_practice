# docstring example
def add(x, y)
    """(float, float) -> float	# type contract
    Returns the sum of x and y	# description
    
    #exemples : at least three examples
    >>>> add(2, 2)
    4
    >>>> add(-2, 3)
    1
    >>>> add(1.2, 3.5)
    4.7
    """
    return round(x + y, 2)

