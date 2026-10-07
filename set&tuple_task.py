#Write Python code to find and print the intersection of the following two sets:
# set_1 = {1,2,3,4,5}
# set_2 = {4,5,6,7,8}
# set_3 = set_1.intersection(set_2)
# print(set_3)

#################################################################################

#Task_2
#Write Python code to find and print the union of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = set1.union(set2)
# print(set3)

######################################################################################

#Task3 : Write Python code to find and print the elements present in set1 but not in
#set2 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1.difference(set2)

print(result)

#########################################################################################

'''Task 4: Write Python code to find and print the symmetric difference of the following
two sets:'''

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# result = set1.symmetric_difference(set2)

# print(result)
############################################################################################

'''Task 5: Write Python code to check if the element 3 is present in the set my_set :
my_set = {1, 2, 3, 4, 5}'''

my_set = {1, 2, 3, 4, 5}

print(3 in my_set)

'''Exercise 1: Exercise 1: Set Intersection
Write a Python script that finds and prints the intersection of two sets.'''

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# intersection = set1.intersection(set2)

# print(intersection)

###################################################################################

'''Exercise 2: Set Union
Write a Python script that finds and prints the union of two sets.'''

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# union = set1.union(set2)

# print(union)

#########################################################################################

'''Exercise 3: Set Difference
Write a Python script that finds and prints the difference between two sets.'''

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# difference = set1.difference(set2)

# print(difference)

#############################################################################################

'''Exercise 4: Set Symmetric Difference
Write a Python script that finds and prints the symmetric difference between
two sets.'''

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# symmetric_difference = set1.symmetric_difference(set2)

# print("Symmetric Difference:", symmetric_difference)

########################################################################################

#Tuple : Create a Tuple: Write a program that creates a tuple containing three
# elements: your name, your age, and your favorite color. Then print the tuple

# name = "Pavan Kumar"
# age = 34
# favorite_color = "Blue"

# my_tuple = (name, age, favorite_color)

# print(my_tuple)

##############################################################################################

'''Access Tuple Elements: Write a program that creates a tuple containing the
days of the week. Then, print the third element of the tuple.'''

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print(days[2])

#################################################################################################\

'''Tuple Concatenation: Write a program that creates two tuples, one
containing odd numbers from 1 to 5 and another containing even numbers
from 2 to 6. Concatenate these two tuples and print the result.'''

# odd_numbers = (1, 3, 5)
# even_numbers = (2, 4, 6)

# result = odd_numbers + even_numbers

# print(result)

####################################################################################################

'''Tuple Unpacking: Write a program that defines a tuple containing the
dimensions of a rectangle (length and width). Then, unpack this tuple into
two variables and calculate the area of the rectangle.'''

# dimensions = (10, 5)

# length, width = dimensions

# area = length * width

# print("Area of the rectangle:", area)

####################################################################################################


'''Check if an Element Exists: Write a program that checks if a given element exists in a tuple.'''
numbers = (10, 20, 30, 40, 50)

# element = 30

# if element in numbers:
#     print("Element exists in the tuple")
# else:
#     print("Element does not exist in the tuple")

#####################################################################################################



