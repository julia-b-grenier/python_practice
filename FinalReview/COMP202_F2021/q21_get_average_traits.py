wizards = {
    'Harry': { 'bravery': 9, 'wit': 5, 'ambition': 6 },
    'Luna': { 'bravery': 7, 'wit': 10, 'ambition': 6 },
    'Draco': { 'bravery': 7, 'wit': -1, 'ambition': 9 },
    'Cedric': { 'bravery': 7, 'wit': 7, 'ambition': 7 }
}

def get_average_traits(d):
    result_d = dict()
    
    for wizard in d:
        for trait in wizards[wizard]:
            if trait not in result_d:
                result_d[trait] = []
                
            result_d[trait].append(wizards[wizard][trait])
            
    for trait in result_d:
        result_d[trait] = sum(result_d[trait])/len(result_d[trait])
    
    return result_d