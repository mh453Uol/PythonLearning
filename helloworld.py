print("Hello World!");
print(1+1-2);

# In python we dont need to specify the type
answer = 42
print(answer);

# This function adds two type however 
# not specifying types has its flaws
def add_numbers(a, b):
    print(a + b)

add_numbers(10, 10)
add_numbers("Majid is ", "life")
#add_numbers(11,"Majid is "); doesnt work type error


# Type Hinting helps Ide but not compiliers
def add_numbers2(a: int,b: int) -> int:
    print(a + b)

add_numbers2(1, 2)

#                   Types in python

# Integer
answer = 42

# Float
pi = 3.14159 

print(answer)
print(pi)

# Float 
print(answer + pi);

#                       CASTING

# Casting from float to int
print(int(pi) == 3)
print(int(pi))
print(int("21")) # 21 as int
print(float("0.123")) #0.123 as float

# Different string syntax
print('HelloWorld' == "HelloWorld" == """HelloWorld""")
# Uppercase first letter
print("hello".capitalize() == "Hello")
print("foo bar".capitalize()) # Foo bar
print("hallo".replace("a","e")) # hello
print("hello".isalpha()) # check if 1 or more alphabetic letter
print("123".isdigit() == True) # useful if convert to int

splittedByComma = "Python,is,weird".split(",")
print(splittedByComma) # array

food = ["tuna","mayo","lunch"]
print(food)

# formatting strings
print("Hi, my name is {0}. I am at {1}".format("Majid", "home"))

name = "Majid"
machine = "MIST"

# name and machine variable are automatically added
sentence = f"Nice to meet you {name}. I am {machine}"
print(sentence)