# python is dynamically typed. It will determin the data type!

# Integers and Floats

# Integer
answer = 42;

# Float 
pi = 3.14159;

# Type casting
piAsInt = int(pi); #3
print(piAsInt); 

answerAsFloat = float(answer); #42.0
print(answerAsFloat); 

# Strings

# All same
me = "Majid";
me2 = 'Majid';
me3 = """Majid""";

print(me,me2,me3);

# utilities

print("hElLo","hElLo".capitalize() == "Hello"); # First Char Uppercase
print("hello".replace("e","*")); # h*llo
print("hello4".isalpha()); # Only Alphabetic
print("1234".isdigit()) # useful for parse to int
print("a,b,c,d,e,f".split(",")); # ["a","b","c",..]

# String formatting

name = "Majid";
machine = "ThinkPad 4280";

# replace 0 with Majid
formatted = "Nice to meet you {0}. I am {1}".format(name,machine);

print(formatted);

# Boolean 
# Capital T and F
pythone_course = True;
java_course = False;

# Same as Javascript 
print(int(pythone_course) == 1);# true is represented as 1
print(int(pythone_course) == 0);# false is represented as 0
print(pythone_course == 1); # JavaScript does this aswell
print(java_course == 0);
print(str(pythone_course) == "True");

# Null

# Use as placeholder later assigned;

aliens_found = None;
print(aliens_found); #None
print(k); #errr k not defined!

