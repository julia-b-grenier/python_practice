def remove_snow(s):
    
    if "\'" in s:
        raise ValueError("There is rain in the string")
    
    no_snow = ""
    
    count_snow = 0
    for i in range(len(s)):
        
        if s[i] in "*." and i != 0:
            if s[i-1] not in "*.":
                count_snow = 0
                
        if s[i] in "*.":
            count_snow += 1
        elif count_snow > 0:
            count_snow -= 1
        else:
            no_snow += s[i]
            
    return no_snow

def second_max(list_nums):
    largest = max(list_nums)
    
    for i in range(list_nums.count(largest)):
        list_nums.remove(largest)
        
    return max(list_nums)