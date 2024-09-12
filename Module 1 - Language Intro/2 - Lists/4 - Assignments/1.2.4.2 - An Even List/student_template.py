import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""

list_length = len(even_list)
print("List length is ", list_length)
list_div_2 = int(list_length/2)

first_middle = even_list[list_div_2 - 1]
second_middle = even_list[list_div_2]

print("First middle value is", first_middle)
print("Second middle value is", second_middle)

# this is the final result. Modify this line, and the empty lines above, to solve the assignment
middle_average = (first_middle + second_middle)/2

# the average of middle elements is
print("The average is: ", middle_average)
