# Python uses intentation rather than brackets !!

number = 5

if number == 5: #required
    print("Number is 5")
else: # required
    print("Number is not 5")

memoryaddress1 = "Register 1";
memoryaddress1Copy = memoryaddress1

# both point to same memory address in memory
print(memoryaddress1 is memoryaddress1Copy)

# Truthy and Falsy Values

if number:
    print("Number is defined and truthy")

if 0:
    print("I will never execute 0 is false")

text = "Hi"

if text: 
    print("Text is defined and truthy")

if "":
    print("I am empty so I will not execute!")

foobar = None

if foobar:
    print("None is falsy")
else:
    print("None is falsy so else will execute")

# Not Equals

if foobar != True:
    print("None in a if is always false however we can negate")

if not foobar: # same as !foobar in other languages
    print("Simpler code")

if 2 == 2 and 1 == 1:
    print("And is same as &&")

if 2 == 2 or 1 == 2:
    print("Or is same as ||")

## Ternary if statement

## 1 == 1 ? "Same":"Not Same C#"

a = 1
b = 2

"bigger" if a > b else "smaller" # Decent

output = "bigger" if a > b else "smaller"; # output get value

print(output)

dynamic_list = [1,2,3,4,5,6]

# loops 

# for loops

## like foreach
for number in dynamic_list:
    print("Current Number is {0}".format(number))

## like typical forloop

for index in range(10):
    print("Index at {0}".format(index))

for index in range(number):
    print(dynamic_list[index])

print(range(10)) # create a list so [1,2,3,4,5,6,7 ..]

# start, stop and step each time
print(range(35,100,2))

# break and continue (like return)

somenumbers = range(0,100*100,100)

print("--------------------------------")

for n in somenumbers: 
    if n == 300:
        print("Found {0} !".format(n))
        break # like return break out of loop
    if n == 200:
        continue # dont execute line 100 when n is 300 
                 # but forloop is still alive
    print("Current iteration number is {0}".format(n))


# While Loops

# While some condition is true

letter = "Majid";

x = 0

while x < 10:
    print("Count is {0}".format(x))
    x += 1