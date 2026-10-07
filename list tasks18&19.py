#Reverse List
my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print(my_list)

#Common Elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
my_list=[]
for i in list1:
    for j in list2:
        if i==j:
            my_list.append(i)
print(my_list)

#Unique Elements
original_list = [1, 2, 2, 3, 4, 4, 5]
un_list=[]
for i in original_list:
    if i not in un_list:
        un_list.append(i)
print(un_list)

#remove duplicates
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
my_list1=[]
for i in duplicated_list:
    if i not in my_list1:
        my_list1.append(i)
print(my_list1)

""" List Concatenation
Write a Python script that concatenates two lists and prints the result."""
list_1=[1,2,3,4]
list_2=[5,6,7,8]
print(list_1+list_2)

""" List Repetition
Write a Python script that repeats a list three times and prints the result"""
list_3=[12,"pythonlife",34,56,576]
print(list_3*2)

""" List Removal
Write a Python script that removes the elements at even indices from a list."""

numbers = [10, 20, 30, 40, 50, 60]

result = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

print("Original list:", numbers)
print("After removing even indices:", result)

""" List Insertion
3
Quiz Questions:
Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of 
a list"""

list_4=[1,2,4,5,6,7]
list_4.insert(0,10)
list_4.insert(1,11)
list_4.insert(2,12)
print(list_4)

# Square Numbers Create a list of squares of numbers from 1 to 10
result=[i**2 for i in range(11)]
print(result)

# Even Numbers Generate a list of even numbers from 1 to 20.
result_1=[i for i in range(1,21) if i%2==0]
print(result_1)
"""Words Lengths Given a list of words, create a list containing the lengths of 
each word."""

words = ["apple", "banana", "cherry", "date"]
result_2=[len(word) for word in words]
print(result_2)
