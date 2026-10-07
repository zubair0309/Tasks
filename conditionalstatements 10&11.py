#Write a Python program that takes a character as input and checks whether it is a vowel or not.
char=input("enter any char: ")
words="aeiouAEIOU"
if char in words:
    print("it is a vowel")
else:
    print("not a vowel")

"""Write a program that takes an age as input and classifies the person into 
one of the following age groups:
Child: 012 years
Teenager: 1317 years
Adult: 1864 years
Senior: 65 years and older"""
age=int(input("enter your age: "))
if age <= 12 and age >=0:
    print("you are child.")
elif age<=17 and age >= 13:
    print(" you are a teenager.")
elif age<=64 and age >= 18:
    print("you are a adult.")
else:
    print(" you are older.")

    """Write a program that takes an integer as input and classifies it as positive, 
negative, or zero. Use the 
if-elif-else statement"""
number=int(input("enter any digit: "))
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("number is zero(0)")

    """Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 400."""
year=int(input("enter the year: "))
if year %400 == 0:
    print("leap year")
elif year % 100 != 0:
    print("not a leap year")
elif year %4 == 0:
    print("leap year")

"""Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation."""
num_1=int(input("enter any digit: "))
num_2=int(input("enter any digit: "))
operator=input("enter operator: ")
if operator=="+":
    print(num_1+num_2)
elif operator=="-":
    print(num_1-num_2)
elif operator=="*":
    print(num_1*num_2)
elif operator=="/":
    print(num_1/num_2)
elif operator=="%":
    print(num_1%num_2)

"""Rewrite the following code using the short-hand 
if statement:
2
Quiz Questions:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd" """
x=8
result="even" if x%2==0 else "odd"
print(result)

"""Write a program that calculates the Body Mass Index BMI using the 
formula: BMI  weight (kg) / (height (m))^2. The program should take 
weight and height as input"""
weight=int(input("enter you are weight: "))
height=float(input("enter you are height: "))
bmi=weight/(height)**2
print(bmi)

"""Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as 
input."""
org_price=int(input("enter price: "))
discount=int(input("enter discount:"))
dis_amount=org_price*discount/100
final_price=org_price - dis_amount
print(f"the final amount is {final_price}")