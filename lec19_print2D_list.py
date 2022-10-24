animals = [['owl', 'bat', 'cow'],
           ['goat', 'duck', 'lion', 'bear'],
           ['panda', 'zebra']]


def print_2D_list(my_list):
    """ list<list> -> NoneType
    Prints all the elements of eaxh sublist of my_list
    one sublist per line
    """
    for sublist in my_list:
        for elmt in sublist:
            print(elmt, end=' ')
        print()

def print_2D_list_2(my_list):
    """ list<list> -> NoneType
    Prints all the elements of eaxh sublist of my_list
    one sublist per line
    """
    for sublist in my_list:
        print(" ".join(sublist))