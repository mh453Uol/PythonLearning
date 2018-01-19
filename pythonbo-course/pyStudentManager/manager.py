students = []
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

def read_file(name):
    try:
        f = open(name,"r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Count not read file")
        f.close()

def save_file(file_name,student):
    f = None
    try:
        f = open(file_name,"a")
        f.write(student + "\n")
        f.close()
    except Exception as e:
        print("Could not save file",e)
        f.close()

#add_student("majid hussain")

read_file("student.txt") # append to students list

print(get_student_titlecase(students));

while True:
    choice = input("Enter Y to add student or N to exit: ")
    if "Y" in choice:
        student_name = input("Enter student name: ")
        student_id = input("Enter id: ")
        #add_student(student_name,student_id)
        save_file("student.txt",student_name)
    else:
        break;

print(get_student_titlecase(students))
