
students = []

def open_file(file_name):
    #           file           access modes
    # w - writing overwrites the entire file
    # r - reading a text file
    # a - appending to a new or existing file
    # rb - reading a binary file
    # wb - writing to a binary file
    try:
        file = open(file_name,"r")
        for line in file.readlines():
            if len(line) > 2:
                line = line[1:-1] 
                get_keyvalues(line,["name","id"]) # preserve the \t and \n
        file.close()
    except Exception as e:
        print("Could not read file",str(e))
        file.close()

def get_keyvalues(dictionary,*args):
    current = ""
    toreturn_dictionary = {}
    i = 0
    while True:
        if i >= len(dictionary) - 2:
            return toreturn_dictionary
        current += dictionary[i]
        if current in args and dictionary[i+1] == ":":
            i += 1
            # get value
            value = ""
            got_value = False 
            while not got_value:
                if dictionary[i] != ",":
                    value += dictionary[i]
                    i += 1
                else:
                    toreturn_dictionary[current] = value
                    got_value = True
        else:
            i += 1  
    return toreturn_dictionary
open_file("/var/autofs/home/s_home/mh453/Python/PythonLearning/pythonbo-course/files/q.txt")