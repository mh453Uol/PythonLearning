#print("Hey welcome to PyStudentManager")
#input("Enter the users name:")
#print("You entered a valid name")

students = []

def titlecase(element: str) -> str:
    to_return = []
    words = element.split(" ")
    for word in words:
        titlecased = word[0].upper() + word[1:].lower()
        to_return.append(titlecased)
    return " ".join(to_return)

def get_students_titlecase(students:[]) -> []:
    students_titlecase = []
    for student in students:
        titlecased = titlecase(student)
        students_titlecase.append(titlecased)
    return students_titlecase

print(get_students_titlecase(students))

# optional function arguments
# same as c# we can add default values

def add_student(name:str, student_id:int = -1):
    student = {"name":name,"student_id":student_id}
    students.append(student)

# I can handle many arguments!
def var_args(name, *args):
    print(name)
    print(args)

# key work args
# Nicely prints out
# passed in keys 
# i.e {'Name': 'Majid', 'Age': 200, 'House': 2}
def key_var_args(**kwargs):
    print(kwargs)
    # if you know ahead of time
    # you can print 
    # each on a new line
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs["house"])

key_var_args(name="Majid",age=200,house=2)

add_student(name="KING RICHARD",student_id=100)
add_student(name="Majid",student_id = 101)
print(students)
var_args("I can","handle many","str","cool")