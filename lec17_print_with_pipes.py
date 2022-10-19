def print_with_pipes(strings):
    """(list<str>) -> NoneType
    Prints out each string of the strings list
    with a pipe character in between each
    >>> print_with_pipes(['A', 'B', 'C'])
    A | B | C
    """
    
    result = ''
    
    for s in strings:
        result = result + s + " | "
    
    print(result[:-3])
    
    #print(" | ".join(strings))