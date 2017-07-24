students = []

def titlecase(element: str) -> str:
    to_return = []
    words = element.split(" ")
    for word in words:
        titlecased = word[0].upper() + word[1:].lower()
        to_return.append(titlecased)
    return " ".join(to_return)    

def add_student(name:str, student_id:int = -1):
    student = {
        "name":titlecase(name),
        "student_id":titlecase(student_id)
        }
    students.append(student)

# reading console
def add_student_ui():
    student_name = input("Enter a student name:")
    student_id = input("Enter a student id:");
    add_student(student_name,student_id)
    print(students)

def what_to_add_student() -> bool:
    user_input = input("Press E to EXIT or C to CONTINUE")
    if user_input == "E" or user_input == "e":
        return False
    return True

file_access_modes = [
    {"appending","a"},
    {"writing","w"},
    {"writing_binary","wb"},
    {"reading","r"},
    {"reading_binary","rb"},
]

def save_file(path,access_mode,text):
    try:
        file = open(path,access_mode)
        file.write(text)
        file.close()
    except Exception:
        print("Count not save file")

def read_file(path,access_mode):
    try:
        file = open(path,access_mode)
        for line in file.readlines():
            print(line)
        file.close()
    except Exception: 
        print("Could not read file")

while True:
    print("\t Current Students:")
    read_file("student.txt","r");
    print("----------------------------------")
    add_student_ui()
    if not what_to_add_student():
        save_file("student.txt","a",str(students) + "\n")
        break



