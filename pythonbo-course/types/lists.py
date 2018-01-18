# List are array under hood when they get bigger it shifts

student_names = ["Majid","Abdul","Fazal"]

print(student_names)

print(student_names[0] == "Majid") # 0 based

print(student_names[-1]) #get last element preety cool
print(student_names[-3])
##print(student_names[-4]) Out of Bounds!

# add string to list
student_names.append("Homer")

print(student_names) # ["Majid","Abdul","Fazal","Homer"]

# Contains

if "Majid" in student_names:
    print("Majid is in list.") 

#len finds length of a list

print("We have {0} elements in our list".format(len(student_names)))

# works on str!
print(len("AAABBBCCC")) # 9

# arrays can handle different types !!!!

student_names.append(1);  # adding int to list
student_names.append(1.0); # adding float to list
student_names.append([1,2,3,4,5]); # adding lists

print(student_names);

# Remove Element shrinks array list by - 1

dynamic_list = [1,2,3,4,5,6]

del dynamic_list[0];

print(dynamic_list,len(dynamic_list)) ## 5

# List Slicing

# ignore first element and give me rest of them so index 1,2,3,4
print(dynamic_list[1:]) # 3,4,5,6

# ignore first and last element 
print(dynamic_list[1:-1]) # 3,4,5
