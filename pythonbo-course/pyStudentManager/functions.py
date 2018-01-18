students = [
    {"name":"majid hussain khattak","id":1},
    {"name":"majid","id":2},
    {"name":"h","id":3},
    {"name":"MAJID HUSSAIN KHATTAK","id":4}
]
countIndex = 0 # this variable is in the main scope

def get_student_titlecase(students):
    titledcased = []
    for student in students:
        print(student)
    return titledcased

def titlecase(name):
    titled = ""
    names = name.split(' ')
    length = len(names)
    for n in range(length):
            titled += names[n][0].upper() + names[n][1:].lower()
            if n < length - 1:
                titled += " "
    return titled

def add_student(name,id = 1):
    # countIndex = countIndex + 1 # this would create a
    # variable in the function scope this is because 
    # python thinks we are assigning a variable 
    # since to assign all you do it write variable name

    if id == 1:
    # To tell python we mean global we do
        global countIndex
        countIndex = countIndex + 1
        students.append({"name": name, "id": countIndex})
    else:
        students.append({"name": name, "id": id})
        
def my_print(*args):
    for arg in args:
        print(arg)

def kwargs_key_word(**kwargs):
    print(kwargs["name"])
    print(kwargs["id"])

add_student("majid",12)
add_student("majid")
add_student("majid")
add_student("majid")

#print(get_student_titlecase(students))

#my_print("majid","is","not","so","good","at","python")
#kwargs_key_word(name = "majid", id = "10", not_printed = "foo")

