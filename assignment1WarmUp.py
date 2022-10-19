def even_and_positive(number):
    """ int ->
    print if the number is even, is positive, is even and positive
    
    >>> 
    Enter a number: -2
    -2 is an even number: True
    -2 is a positive number: False
    -2 is a positive even number: False
    
    >>> 
    Enter a number: 7
    7 is an even number: False
    7 is a positive number: True
    7 is a positive even number: False
    
    >>> 
    Enter a number: -3
    -3 is an even number: False
    -3 is a positive number: False
    -3 is a positive even number: False

    """
    
    even = False
    positive = False
    if number % 2 == 0:
        even = True
    if number > 0:
        positive = True
        
    print(number, "is a even number: ", even)
    print(number, "is a positive number: ", positive)
    
    print(number, "is a even and positive number: ", even and positive)
    
even_and_positive(int(input("Enter a number: ")))