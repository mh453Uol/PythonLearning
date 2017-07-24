def read_file():
    try:
        file = open("student.txt","r")
        for line in student_read(file):
            print(line)
        file.close()
    except Exception: 
        print("Could not read file")

# yield returns just one student at a time
# so inside read_file for we get one student
# execution for this func is paused and then value passed to 
# line variable and it does some operation
# and repeat
def student_read(file):
    for student in file:
        print("Getting Student ***")
        yield student

read_file()