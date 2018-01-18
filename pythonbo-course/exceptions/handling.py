
student = {
    "name":"Majid",
    "id":12,
    "feedback":None
}

try:
# EXCEPTION ! KEY ERROR DONT EXIST
    last_name = student["lastname"]
except KeyError as error:
    print("Error finding lastname")
    print(error)
except TypeError as error:
    print("I cant add these two together")
    print(error)
except Exception as error:
    # handles all errors
    print("Unknown Exception")
    print(error)

print("This code executes")

#add to dictionary

student["lastname"] = "h"
