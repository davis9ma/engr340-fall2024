"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""
from statistics import stdev

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
# import numpy as np

# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

### YOUR CODE HERE

# find the stdev of the lists
list_A_stdev = stdev(random_list_A)
print("list A stdev is ",list_A_stdev)
list_B_stdev = stdev(random_list_B)
print("list B stdev is",list_B_stdev)
#using if else, find the list with the highest stdev.

# set this variable equal to the list with the largest standard deviation
# do not modify this variable's name, you can/should adjust the contents ;)
# e.g. longest_list_is = myList
if list_A_stdev > list_B_stdev:
    longest_list_is = random_list_A
    print("List A has the highest standard deviation!")

else:
    longest_list_is = random_list_B
    print("List B has the highest standard deviation!")
### YOUR CODE HERE
