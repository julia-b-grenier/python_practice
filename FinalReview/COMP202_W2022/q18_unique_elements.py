def unique_elements(d):
    all_elmt = []
    
    for l in d.values():
        for elmt in l:
            all_elmt.append(elmt)
    unique = []
    for elmt in all_elmt:
        if (all_elmt.count(elmt) == 1 and
            elmt not in unique):
            unique.append(elmt)
            
    return unique


d =  {'a': [1, 3, 7, 9], 'b': [3, 6, 5, 3, 2], 'c': [6, 7, 8], 'd': [0, 1, 0]}


print(unique_elements(d))
    