matrix = [[2,3,9], [5,1,6], [8,-1,9]]

def min_elements(my_list):
    """ (list<list<int>>) -> list<int>
    Returns a list containing the smallest integer
    of each sublist of my_list.
    
    """
    
    smallest_numbers = []
    
    """
    for i in range(len(my_list)):
        current_smallest = my_list[i][0]
        for j in range(len(my_list[i])):
            if my_list[i][j] < current_smallest:
                current_smallest = my_list[i][j]
        smallest_numbers.append(current_smallest)
    """
    
    
    
    for sublist in my_list:
        smallest_numbers.append(min(sublist))
    
    
    
    """
    for sublist in my_list:
        current_smallest = sublist[0]
        
        for elmt in sublist:
            if elmt < current_smallest:
                current_smallest = elmt
        
        smallest_numbers.append(current_smallest)
    """
    
    return smallest_numbers