
def read_unique_lines(filename):
    """ (str) -> list<str>
    Write a function that takes as input the filename of a file
    containing one phrase per line. The function should return
    a list of the phrases, without duplicates.
    
    #if we uses doctest : leaves result on one line and have to create the file used (no external file, self-contained)
    
    >>> fobj = open("quotes.txt", "w") # mode "w" for writing => delete content
    >>> fobj.write("My first line in a file!!\\n"This will appear on the second line(?)") #needs to use a backslash
    31 # number of characters written counts \\n as one
    >>> fobj.close()
    >>> read_unique_lines("quotes.txt")
    
    """
    
    strings = []
    
    fobj = open(filename, "r")
    
    for line in fobj:
        line.strip() # remove "\n" that is read by fobj
        print(line) 
        if line not in strings:
            strings.append(line)
    
    
    fobj.close()
    
    return strings

def write_strings_to_file(string_list, filename):
    """ (list<str>, string) -> NoneType

    Write a function that takes a list of strings as input as well
    as a filename. The function should write to the file all the
    elements of the list, one per line.
    
    >>> write_strings_to_file(["abc", "def", "ghi"], "write_strings.txt")
    """
    
    fobj = open(filename, "w")
    for s in string_list:
        fobj.write(s + "\n")
    fobj.close
    

def write_strings_to_file_using_join(string_list, filename):
    """ (list<str>, string) -> NoneType

    Write a function that takes a list of strings as input as well
    as a filename. The function should write to the file all the
    elements of the list, one per line.
    
    >>> write_strings_to_file_using_join(["abc", "def", "ghi"], "write_strings.txt")
    """
    
    fobj = open(filename, "w")
    s = "\n".join(string_list)
    fobj.write(s)
    fobj.close
    
    
    