import math

def isAMultiple(x,y):
    """(int, int) -> bool
    Returns whether it is true or false that x is a multiple of y
    
    >>>> 8
    >>>> 4
    true
    
    >>>> 10
    >>>> 4
    false
    
    >>>> -8
    >>>> 2
    true

    """
    
    return (x % y) == 0


#print(isAMultiple(int(input("Enter a number ")), int(input("Enter another number "))))


def isSquareRootInteger(x):
    """(int) -> bool
    Evaluates to True when the square root of the value stored in the variable x is an integer
    
    >>>> 4
    true
    
    >>>> 10
    false
    
    >>>> 9
    true

    """
    #print(math.sqrt(x), math.sqrt(x)//1, math.sqrt(x) == math.sqrt(x)//1)
    return math.sqrt(x) == math.sqrt(x)//1

#print(isSquareRootInteger(int(input("Enter a number: "))))
    
def nearestToTen(num1, num2):
    """(int) ->
    Takes 2 integers x and y as input and prints whichever value is the nearest to 10.
    It prints 0 in case of a tie
    
    >>>> 4
    >>>> 8
    8
    
    >>>> -3
    >>>> -6
    -3
    
    >>>> 6
    >>>> 6
    0

    """
    
    if num1 < num2:
        print(num2)
    elif num1 > num2:
        print(num1)
    else:
        print(0)
    
#nearestToTen(int(input("Enter num1: ")), int(input("Enter num2: ")))


def zoneNuclearPlant(plant_x, plant_y, pos_x, pos_y):
    """(int) ->
    Takes 2 integers x and y as input and prints whichever value is the nearest to 10.
    It prints 0 in case of a tie
    
    >>>> 0
    >>>> 0
    >>>> 50
    >>>> 0
    Ingestion Planning Zone
    
    >>>> 0
    >>>> 0
    >>>> 2
    >>>> 0
    Automatic Action Zone
    
    >>>> 0
    >>>> 0
    >>>> 3
    >>>> 4
    DEtailed Planning Zone

    """
    
    distance_from_plant = math.sqrt(abs(plant_x-pos_x)**2 + abs(plant_y-pos_y)**2)
    if distance_from_plant <= 3:
        return "Automatic Action Zone"
    elif distance_from_plant <= 10:
        return "Detailed Planning Zone"
    elif distance_from_plant <= 20:
        return "Contingency Planning Zone"
    elif distance_from_plant <= 50:
        return "Ingestion Planning Zone"
    else:
        return 0
    
print(zoneNuclearPlant(0,0,3,0))