wizards = {
    'Harry': { 'bravery': 9, 'wit': 5, 'ambition': 6 },
    'Luna': { 'bravery': 7, 'wit': 9, 'ambition': 6 },
    'Draco': { 'bravery': 7, 'wit': 0, 'ambition': 9 },
    'Cedric': { 'bravery': 7, 'wit': 7, 'ambition': 7 }
}

def sorting_hat(d_wizards):
    
    result = [0,0,0,0]
    
    for charact in d_wizards.values():
        
        if charact['bravery'] == 9:
            result[0] += 1
            
        elif charact['wit'] == 9:
            result[1] += 1
            
        elif charact['ambition'] == 9:
            result[2] += 1
            
        else:
            result[3] += 1
            
    return tuple(result)