# List a collection of elements
student_names = []

# You can have different types 
# Initializing a list
student_names = ["Mark","Katarina","Jessica",1]

print(student_names)

# Get index of list
# student = student_names[1]
# print(student)

# First Element
print(student_names[0])

# Last Elements so 1
print(student_names[-1])
# Second Last Element so "Jessica"
print(student_names[-2])
# Third Last ELement so "Katarina"
print(student_names[-3])

# Loops

# for loop
# Very similar to foreach(var name in names)
for name in student_names:
    print("Student name is {0}".format(name))

length_of_list = len(student_names)-1
cut = int(length_of_list/2)
print(student_names[cut])

x = 0

# similar to for loop 
# for(start, end condiction, step/increment)

# range you have a start value, end value and step
# so when you do range(0,10,1) behind the scene
# python creates an array so [0,1,2,3,4,5,6,7,8,9,10]
for index in range(0,10,1):
    x += 10
    print("The value of X is {0}".format(x))

# stop for loop to stop or start
for name in student_names:
    if name == "Mark":
        print("Found Mark")
    print("Currently Iterating {0}".format(name))

# What about break out of for loop

for name in student_names:
    if name == "Mark":
        print("Found Mark")
        break
    print("Currently Iterating {0}".format(name))

# What about not printing someone but
# still printing other in the list

for name in student_names:
    if name == "Jessica":
        # Continue continutes the iteration
        # all lines below in block will not run
        continue;
        print("Found Jessica") # not runned because of continue
    print("Currently Iterating {0}".format(name))

