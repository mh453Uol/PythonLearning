students = []
# classes start with class keyword
class Student:
    name : str
    id: int
    # methods start with self 
    # this is a constructor
    def __init__(self,username:str, student_id:int = -1):
        name = username
        id = student_id
        student = { "name":username,"student_id":student_id }
        students.append(student)
        
    # to string in python
    def __str__(self):
        return "Student"

majid = Student("Majid",1)
print(majid)
david = Student("David")
print(david)
print(students)

