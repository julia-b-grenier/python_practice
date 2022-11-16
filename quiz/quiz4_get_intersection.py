import doctest

def get_intersection(sets):
    """
    >>> get_intersection([[1,3,6], [1,2,3,5,6], [1,2,3]])
    [1, 3]
    """
    i = [] # D1
    
    if len(sets) == 0: # G1
        return i
    
    for e in sets[0]: # E1
        b = True # I2
        for s in sets: # J2
            if e not in s: # H3
                b = False # B4
        if b: # C2
            i.append(e) # K3
            
    return i # A1
    
    
doctest.testmod()
