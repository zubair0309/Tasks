#QUIZ QUESTIONS                       
#<Q1>what do identity operators (is and is not check in python)?
user_name=123
user_id=1234
print(user_name is user_id)
print(id(user_id))
print(id(user_name))
#a)value equality b)memory address identity c)type equality d)sequence membership .answer (b).

#<Q2>which of the following statements is correct for the identity operator is?
#a)x is y true if the values of x and y are equal.
#b)x is y true if x and y refer to the same object.
#c)x is y is true if the type of x and y is the same.
#d)x is y true if x and y are both none. answer(b)

#<Q3>what do membership operators (in and not in )check in python?
# a)memory address identity b)type equality c)valu equality d)sequence membership.answer(d)

#which memebership operator is used to check if value is not  present in sequence?
# a)in b)not in .answer(b).


#CODING EXCERCISE
#<Q1>create a program that takes user input for their name and age.use formatted strings(f-strings) to print a message welcoming the user and stating the age.
user_name=input("enter your name:")
user_age=input("enter your age:")
print(f"welcome to pythonlife {user_name}. your age is {user_age} .")
'''OUTPUT:
enter your name:sony
enter your age:22
welcome to pythonlife sony. your age is 22 .'''

#<Q2>create a list called numbers that contains integers from 1 to 10.
#check if the number 5 is in the list.
#check if the number 15 is not  in the list.
numbers=[1,2,3,4,5,6,7,8,9,10]
print(5 in numbers)
print(15 not in numbers)
'''OUTPUT:
True
False'''