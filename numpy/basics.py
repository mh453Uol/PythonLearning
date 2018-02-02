import numpy as np

print(np.array([1,2,3,4]))

# only importing one feature from a whole package 
from numpy import array

# no need to use prefix
print(array([1,2,3]))

height = [1.73,1.68,1.71,1.89,1.79] #kg
weight = [65.4,59.2,63.6,88.4,68.7] #m

# power of numpy
# can calculatation on lists dont need to 
# access each index numpy does it all for us

# numpy can do this because it assumes list is 
# of one type e.g int 
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

print(bmi)

print(np_height + np_height) 
# add 1.73 + 1.73 for index 1
# add 1.68 + 1.68 for index 2

print(bmi[0]) # getting index 0 from numpy list
# same behaviour as lists

print(bmi > 23) # returns boolean array
# [False False False  True False]

print(bmi[bmi > 23]) 
# bmi[predicate]
# returns values as list
# where predicate returns true

names = ["majid","tom","richard","harry"]
weight = [10.1,10.2,10.3,10.4] # stones
height = [5.6,5.10,5.11,5.10] #foot

np_weight_lbs = np.array(weight) * 14
np_height_inchs = np.array(height) * 12

bmi = (np_weight_lbs / np_height_inchs ** 2) * 703

print(bmi)

print(np.array([True,1,2]) + np.array([1,2,False]))
# True -> 1 
# False -> 0
# so [2,3,2]

print(type(np.array([1,2,3,4,5,6,7,8,9])))
# numpy.ndarray which means n-dimensional array

# 2d numPy Lists
multiples = [[1,2,3],
             [4,5,6],
             [7,8,9]]

print("Arrays set up")
print(multiples[0][0:3])
print(multiples[1])
print(multiples[2])
np_board = np.array(multiples)
print(np_board.shape) #(3 rows and 3 columns)

print(np_board[0,3]) # 3 [0 row] and [3rd column]






