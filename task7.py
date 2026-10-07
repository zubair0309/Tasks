# 1. Write a Python program that prints your name.
print("Mahesh")
"""
output:
mahesh
"""

# 2. Create a Python script with both single-line and multi-line comments.
# Explaning the purpose of the script

# Below code is used to perform basic arithmetic operations
num_1 = 10
num_2 = 5
result = num_1 + num_2  # Addition
print("The result of addition is:", result)
"""
output:
The result of addition is: 15
"""

# 3. Define a list containing three data types: integer, string, and float. Print the list and its data types.
my_list = [42, "Hello, World!", 3.14]
print(my_list)
"""
output:
[42, 'Hello, World!', 3.14]
"""

# 4. Define a set containing employee id's.
employee_ids = {101, 102, 103, 104}
print(employee_ids)
"""
output:
{101, 102, 103, 104}
"""

# 5. Concatenate two strings and print the result.
name_1 = "Mahesh"
name_2 = "Malavika"
result = name_1 + name_2
print(result)
"""
output:
MaheshMalavika
"""

# 6. Create a variable with a name that is a Python keyword. what happens?
#class = "This is a class variable"
#observation: The above line will raise a SyntaxError because 'class' is a reserved keyword in Python and cannot be used as a variable name.

# 7. Declare two variables, one  storing an integer and the other a string.
# print their values.
age = 21
print(age)
user_name = "Mahesh"
print(user_name)
"""
output:
21
Mahesh
"""

# 8.Convert a float to an integer and print the result.
length=5.8
print(length)
print(type(length))
sample=int(length)
print(sample)
print(type(sample))
"""output:
5.8
<class 'float'>
5
<class 'int'>
"""

# 9.Convert an integer to a string and display the output.

person_age=22
print(person_age)
print(type(person_age))
sample=str(person_age)
print(sample)
print(type(sample))
"""
output:
22
<class 'int'>
22
<class 'str'>
"""

# 10.Take the user's age as input and print a message using that input.

user_age=input("enter your age:")
print("your age is",user_age)
"""
output:
enter your age:25
your age is 25
"""

# 11.Write a program that prints a pattern using multiple print statements.

print("*")
print("**")
print("*")
print("**")
print("***")
"""
output:
*
**
*
**
***
"""

# 12.Create a Python script for a simple task and add comments to
#explain each step.

#store the first number
num_1=10
#store the second number
num_2=10
#add the two numbers
result=num_1+num_2
#print the result
print(result)
"""
output:
20
"""

# 13.Implement a program that uses a dictionary to store information
#about a book (title, author, publication year)

sample_book={
"title":"python",
"author":"vasu",
"publication_year":2026
}
print(sample_book)
print(type(sample_book))
"""
output:
{'title': 'python', 'author': 'vasu', 'publication_year': 2026}
<class 'dict'>
"""

# 14.Write a python program that takes a string as input( 35 )and return
#float value

value=input("enter a value:")
sample=float(value)
print(sample)
print(type(sample))
"""
output:
enter a value:35
35.0
<class 'float'>
"""

#15.Write a program to take two names as input and print them together.

name_1=input("enter first name:")
name_2=input("enter second name:")
result=name_1+name_2
print(result)
"""
output:
enter first name:mahesh
enter second name:malavika
maheshmalavika"""

#16.Create a program that takes user input for their age, converts it to
#an integer, adds 5, and then prints the result

user_1=input("enter your age:")
sample=int(user_1)
result=sample+5
print("age after 5 years:",result)
"""
output:
enter your age:25
age after 5 years: 30
"""


# 17.Build a calculator program that takes two numbers as input and
#performs the arithmetic operation
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
add_operation=num_1+num_2
print("addition:",add_operation)
sub_operation=num_1-num_2
print("subsraction:",sub_operation)
mult_operation=num_1*num_2
print("multiplication:",mult_operation)
div_operation=num_1/num_2
print("division:",div_operation)
"""
output:
enter first number:10
enter second number:5
addition: 15
subsraction: 5
multiplication: 50
division: 2.0
"""