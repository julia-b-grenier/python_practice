def is_polygonal(n,num_sides):
    if num_sides <= 2:
        return False
    
    x = num_sides - 2
    p = 1
    i = x + p
    
    while p < n:
        p += i
        i += x
        
    return p == n
        