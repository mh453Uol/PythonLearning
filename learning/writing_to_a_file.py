file_access_modes = [
    {"appending","a"},
    {"writing","w"},
    {"writing_binary","wb"},
    {"reading","r"},
    {"reading_binary","rb"},
]

def save_file():
    try:
        file = open("student.txt","a")
        file.write("hey" + "\n")
        file.close()
    except Exception:
        print("Count not save file")

def read_file():
    try:
        file = open("student.txt","r")
        for line in file.readlines():
            print(line)
        file.close()
    except Exception: 
        print("Could not read file")

save_file()
read_file()