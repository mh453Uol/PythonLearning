students = [
    {"name":"suhan alI SHAH","id":1},
]
countIndex = 0 # this variable is in the main scope

def get_student_titlecase(students):
    titledcased = []
    temp = None
    for student in students:
        temp = student
        temp["name"] = titlecase(temp["name"])
        titledcased.append(temp)

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

add_student("majid hussain")

print(get_student_titlecase(students));

while True:
    choice = input("Enter Y to add student or N to exit: ")
    if "Y" in choice:
        student_name = input("Enter student name: ")
        student_id = input("Enter id: ")
        add_student(student_name,student_id)
    else:
        break;

print(get_student_titlecase(students))
