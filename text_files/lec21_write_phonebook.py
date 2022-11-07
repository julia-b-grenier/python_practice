
def write_phonebook():
    """ () -> NoneType

    The function will keep asking the user to enter contact names and numbers until they enter 'stop'.
    • Each contact name and number should be saved into a file called phonebook.csv, with the name and number separated by a comma, and one name/number pair per line.
    • The function should not delete any existing data from the file.
    """
    
    fobj = open("phonebook.csv", "a")
    
    while True:
        name = input("Enter contact name: ")
        if name == "stop":
            break
        number = input("Enter number: ")
        
        fobj.write(name + "," + number)
        
    fobj.close()
    
    