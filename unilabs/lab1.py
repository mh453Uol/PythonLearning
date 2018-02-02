x = 8.5 
print(type(x)) #float
print(x.is_integer()) #false

print(type(8)) #int
print(type(True)) #bool
print(type("Hello")) #str

# we can change type multiple types of variables!
n = 3
n = 5.3
n = "Hello"
print(n) # Hello 
print(type(n)) # str

print("We will have a feast tonight unless you say OK")
speed = "This is the current speed"
bad_name = 5

def toFahrenheit(celsuis):
    return celsuis * (9/5) + 32

print(toFahrenheit(20) == 68)
print(toFahrenheit(40) == 104)

def money_earned(hours_worked, hourly_rate):
    total = 0

    if hours_worked > 40:
        overtime = hours_worked - 40;
        total += overtime * (hourly_rate * 1.5)
        hours_worked = hours_worked - overtime

    total += hours_worked * hourly_rate
    return total

print(money_earned(100,5)) 
print((40 * 5) + (60 * (5 * 1.5)))

def terminal_input():
    total = 0
    count = 0
    while True:
        user_input = input("Enter a number: ")
        try:
            entered = int(user_input)
            total += entered
            count += 1
        except Exception:
            if(user_input == "done"):
                print(str.format("{1} {2} {3}",total,count,total/count))
            else:
                print("Enter done is you want to finish else type a number")

#terminal_input()

import math
import numpy as np
import matplotlib.pyplot as plt

print(math.pi) #pi value

# creates random values in shapes as 
# 2 rows and 3 columns
x = np.random.rand(2,3)
# since x is a 2d array we specify the axis (values)
# as first columns
y = np.mean(x,0)
print(y)

#plt.plot(y)
#plt.show()

# create random values with 
# mean (average) of 1.75 
# standard deviation (max from mean)
# and amount of random numbers is 10
print(np.random.normal(1.75,0.20,10))

from numpy import linspace
x = linspace(0, 1, 100) # make 100 points between 0 and 1.

values = linspace(-4,4,10)
values = (values **3) - 4

plt.plot(values)
plt.show()

m1 = np.linspace(1,100,10)
m2 = np.linspace(2,4,10)

plt.scatter(m1,m2)
plt.show()

print(values)