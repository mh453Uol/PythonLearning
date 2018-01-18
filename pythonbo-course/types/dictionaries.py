# dictionary like JSON

# key value pair
# structured data 

student = {
    "name": "Mark",
    "student_id":1000,
    "feedback":None
}

students = [
    { "name": "Majid", "id":1},
    { "name": "John", "id":2},
    { "name": "Johnes", "id":3},
    { "name": "Tupled", "id":4},
]

for x in students:
    print("Student -> id: {0}  name: {1}".format(x["id"], x["name"]))

# if key doesnt exist unknown is returned
print(student.get("d","Unknown")) 

# see all keys
print(student.keys())
print(student.values())

# get all keys and then values
for x in student.keys():
    print(student[x])

# deleting keys

del student["name"]

print(student) # {id: .. , feedback: ..}

