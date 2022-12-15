

def same_parity(list_nums):
    if type(list_nums) != list or len(list_nums) == 0:
        raise ValueError()
    
    for i in range(len(list_nums)-1):
        
        if (type(list_nums[i]) != int or
            type(list_nums[i+1]) != int or
            list_nums[i] <= 0 or list_nums[i+1] <= 0):
            
            raise ValueError()
        
        if (list_nums[i] % 2 != list_nums[i+1] % 2):
            return False
        
    return True
    
    