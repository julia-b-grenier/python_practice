# Binary search
# time to do it : log(n)
# time to do a linear search n

sequence = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]

def middle_index(low,high):
    return (low + high)//2

def binary_search(sequence, item_to_search):
    low = 0
    high = len(sequence) -1
    
    while low <= high:
        middle = (low + high) // 2
        
        if sequence[middle] < item_to_search:
            low = middle + 1 
        elif sequence[middle] < item_to_search:
            high = middle - 1
            
    return middle
    