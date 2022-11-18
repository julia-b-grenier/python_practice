
class Student:
    PASSING_GRADE = 55
    num_students = 0
    
    def __init__(self, name="No name", mcgID="0", new_courses = []): # Constructors with optional arguments
        print("Creating a new student")
        print(id(self))
        self.name = name
        self.mcgillID = mcgID
        
        self.courses = []
        
        for course in new_courses:
            courses.append(course)
        
        Student.num_students += 1
        
    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.mcgillID)
        
    def update_name(self, new_name):
        self.name = new_name
        
    def add_course(self, course):
        self.courses.append(course)
        
        
s = Student("Julia", "261113244")
print(id(s), s.name, s.mcgillID)
print(Student.PASSING_GRADE)
print(s.display_info())
s.update_name("Julia B.Grenier")

print(s.name)