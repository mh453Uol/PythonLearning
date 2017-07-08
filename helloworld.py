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

# Boolean and none

is_sunny = True;
is_windy = False;

if(is_sunny):
    print("Its sunny today");

# Casting Booleans

#int(isSunny) returns 1 is true or 0 if false
if(int(is_sunny) == 1):
    print("Its Sunny Today");

if(int(is_sunny) == 0):
    print("Its Not Sunny Today");

#str(isSunny) returns "True"

if(str(is_sunny) == "True"):
    print("Its Sunny Today");

# Null or None

# Null are good for placeholders
aliens_found = None

# having a unassigned variable is 
# illegal in python
# This doesnt work (below)
# _is_aliens_found = ""

# Another if style

numer = 5

if numer == 5:
    print("Number is 5")
else:
    print("Numer is NOT 5")

# Truthy and Falsy Values

# Truthy 
#   - Number which is > 0
#   - String which lenght is > 0
#   - List or array length > 0

#Falsy
#   - Number which is < 0
#   - String which is empty
#   - List or array length < 0
#   - None

number = 0
if number:
    print("This will NOT execute because of falsy")

if "":
    print("This will NOT execute because of falsy")

if []:
    print("This will NOT execute because of FASLY")

if None:
    print("This will NOT execute because of FALSY")

if number != 0:
    print("This will NOT execute because number is 0")

# aliens_found = false so not is like !aliens_found
if not aliens_found:
    print("Let wait til 2020")

# multiple conditions
if not aliens_found and number == 0:
    print("This will execute since aliens are not found and number is equal to 0")

if True or False:
    print("This will execute since its a XOR")

# Tenary If Statement

a = 1
b = 2

# In english bigger if a > b else smaller
output = "bigger" if a > b else "smaller"
print(output)

