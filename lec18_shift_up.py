def shift_up(my_list):
    """ (list<int>) -> NoneType
    Shifts up all elements of my_list. (The last element
    of my_list will become the first element.)
    
    >>> numbers = [1, 2, 3, 4, 5]
    >>> shift_up(numbers)
    >>> numbers
    [5, 1, 2, 3, 4]
    
    """
    
    # TypeError you cannot add one integer to a list
    #my_list[:] = my_list[-1] + my_list[:-1]
    
    
    
    my_list[:] = [my_list[-1]] + my_list[:-1]
    
    """
    Method 2
    
    last_num = my_list[-1]
    
    for i in range(len(my_list)-1, 0, -1):
        my_list[i] = my_list[i-1]
    my_list[0] = last_num
    
    """