class Student:
    """ a new data type"""
    
    
    
def create_Student(name, mcgID):
    """ (str,int) -> Student
    Creates and returns a new Student object with the given name and mcgill ID
    
    >>> bob = create_Student("Bob", 260)
    >>> type(bob)
    <class '__main__.Student'>
    
    """
    
    s = Student()
    s.name = name
    s.mcgillID = mcgID
    
    return s


def name_with_larger_ID(s1, s2):
    
    if s1.mcgillID > s2.mcgillID:
        return s1.name
    
    return s2.name