def swap_elements(my_list, i, j):
    """ (list, int, int) -> NoneType
    Swap the elements at indices i and j of my_list.
    Modifies the input list directly.
    
    >>> swap_elements([5, 1, 4], 0, 2) # the list will be garbage collected since its a local variable
    
    >>> numbers = [5, 1, 4]
    >>> swap_elements(numbers, 0, 2) # +numbers and my_list will be aliases
    >>> numbers
    [4, 1, 5]
    """
    
    temp_var = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp_var
    
def swap_elements_no_modification(my_list, i, j):
    """ (list, int, int) -> list
    Swap the elements at indices i and j of my_list.
    Returns the new list and does not modify the input list.
    
    >>> numbers = [5, 1, 4]
    >>> swap_elements_no_modification(numbers, 0, 2) # +numbers and my_list will be aliases
    [4, 1, 5]
    >>> numbers
    [5, 1, 4]
    """
    
    # first way to copy a list
    my_list_copy = []
    for x in my_list:
        my_list_copy.append(x)
        
    # A slice is a copy
    #my_list_copy = my_list[:]
    
    temp_var = my_list_copy[i]
    my_list_copy[i] = my_list_copy[j]
    my_list_copy[j] = temp_var
    
    return my_list_copy