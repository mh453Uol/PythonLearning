import re

a = "Monty Python"
print(a[0])  # M

print(a[0:3])  # Mon
# 012 stops before index 3

print('o' in a)  # True o is in Monty Python

print(a.lower())

print(a.find('n'))  # 2 first n is at index 2

print("In %d years, I have spotted %g %s" % (3, 0.1, "camels"))
print("In {0} year, I have spotted {1} {2}".format(3, 0.1, "camels"))

# extract the portion of the string after the colo
spamConfidence = ' X-DSPAM-Confidence: 0.8475 '
index = spamConfidence.find(":")

if index != -1:
    content = spamConfidence[index+1:]
    content = content.strip()
    content = float(content)
    print(content)

# listings are mutable so you can add,remove etc
set = [2, 4, 8]
set[0] = 100

print(set)

setTwo = set

print(setTwo)

# adding to list
print(3 << 2)

# 21 <- Binary Units
# 11 <- Binary Representation

# 8421 <- Binary Units
# 1100 <- Binary Representation

print(6 >> 1)

# 421 <- Binary Units
# 110 <- Binary Representation

# 421 <- Binary Unit
# 011 <- Binary Representation

# pointers
x = [1, 2, 3]

y = x

x.append(4)

print(x is y)
print(x, y)


def consoleInput():
    entered_in_console = []
    while True:
        entered = input("Enter a number: ")
        try:
            parsed_number = int(entered)
            entered_in_console.append(parsed_number)
        except Exception:
            smallest = None
            largest = None
            for n in entered_in_console:
                # first set smallest and largest
                if smallest is None or largest is None:
                    smallest = n
                    largest = n

                if n < smallest:
                    smallest = n

                if n > largest:
                    largest = n

                print("Smallest: ", smallest)
                print("Largest: ", largest)
            break


# consoleInput()


# dictionary think JSON object key value

dict = dict()
dict[0] = "zero"
dict[1] = "one"
dict[2] = "three"
dict["foo@bar.com"] = "majid"


print(dict.keys())
print(dict.get("foo@bar.com"))  # get value by key

cars = [
    # this is object like javascript
    {"manufacture": "BMW", "cars": [
        {"manufacture": "BMW", "car": "M3"},
        {"manufacture": "BMW", "car": "M1"},
        {"manufacture": "BMW", "car": "M3 Sport"}
    ]},
    {"manufacture": "Tesla", "cars": [
        {"manufacture": "Tesla", "car": "Model 3"},
        {"manufacture": "BMW", "car": "Model x"},
        {"manufacture": "BMW", "car": "Roadster"}
    ]},
]

print(cars[0].get("cars")[0].get("car"))

def word_count(words):
    count = {}

    for letter in words:
        
        if count.get(letter,None) is None:
            # doesnt count key so add it
            count[letter] = 1
        else:
            #key exist so increment count
            value = count[letter]
            value += 1
            count[letter] = value
    print(count)
word_count("From the farm, I saw the first sheep while I was the first farmer in the place")

#file handling

def word_count_on_file(file_name):
    counts = {}
    # open file in read mode
    file = open(file_name,"r")
    # iterate through each line
    for line in file.readlines():
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] = counts[word] + 1
    print(counts)
    file.close()

word_count_on_file("random_text.txt")

def word_count_without_punctutation(file_name):
    count = {}
    file = open(file_name,"r")
    # last element \" is escaped "
    punctutation = ".,?!';.-"
    output = "@@@@@@@@"

    # iterate through each line
    for line in file.readlines():
        words = line.split()
        for word in words:
            x = word.maketrans(punctutation,output)
            print(word.translate(x))
    file.close()

word_count_without_punctutation("random_text.txt")


# regular expression

emails = "foobar@foo.com,bar@bar.com,me@ge.com"

email = emails.split(",")

for e in email:
    xp = e.rstrip()
    if re.search("@",xp):
        print(xp)
