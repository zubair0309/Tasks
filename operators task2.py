#QUIZ QUESTIONS
#<Q1>What is the  value of result in the following code?
x=15
y=4
result=x//y
print(result)
#a)3.75 b)3 c)4 d)4.5
#15/4=3.75 (floor divison gives int type so anser is 3 option(b))

#<Q2>what is the ouput of the following code?
a=7
b=3
c=a%b
print(c)
#a)2 b)1 c)3 d)4
#remainder 1 quotient 2 .answer(b)

#<Q3>which assigment operator is equivalent to x=x*5?
#x*=5==>x=x*5
#a)x**=5 b)x//5 c)x*=5 d)x%=5.answer(c)

#<Q4>what is the result of expression 5<3 or 2==2?
#5<3 false or 2==2 true ..in or operator any one true gives true.T OR F=T
a=5<3
b=2==2
c=a or b
print(c)
#a)true b)false c)error d)none .answer(a)

#<Q5>if a=true and b=false what is the  value of not a or b?
a=10>5
b=5>10
print(a,b)
print(a or b)
print(not a  or  b)
'''output:
True False
True
False'''
#a) true b)false c)error d)none .answer(false).

#CODING EXCERCISE
#<Q1>write a python program to calculate the area of rectangle using the given formula area=lenght * width .take the values of lenght and width as inputs from the user.
print("           -----hiii viewer-----        ")
lenght=int(input("please enter lenght(in ft):"))
width=int(input("please enter width(in ft):"))
area=lenght * width
print(f"THANKYOU FOR ENTERING  DATA ....LENGHT  {lenght}ft,WIDTH  {width}ft ARE YOUR SITE DIMENSIONS.AREA OF SITE IS {area}fts. ")
'''output:
           -----hiii viewer-----        
please enter lenght(in ft):15
please enter width(in ft):45
THANKYOU FOR ENTERING  DATA ....LENGHT  15ft,WIDTH  45ft ARE YOUR SITE DIMENSIONS.AREA OF SITE IS 675fts.''' 

#<Q2>write a program to demonstrate incrementing and decrementing a variable .
a=43
b=45
a+=1 #a=a+1
b-=1 #b=b-1
print(a)
print(b)


#<Q3>write a program to  convert temperature from celsius to fahrenheit.the formula  for conversion is :F=(C*9/5)+32.Take temperature in celsius as input from user.
c = float(input("enter you temperature in C:"))
f=(c*9/5)+32
print((f) ,"fahrenheit")
print(f"you are having temperature of {f}fahrenheit.get well soon . . . . .  ")       
'''output:
enter you temperature in C:101.2
214.16000000000003 fahrenheit
you are having temperature of 214.16000000000003fahrenheit.get well soon . . . . .   '''


#<Q4>write a program to calculate the simpple interest given the principal amount,rate,time in years.
principal=float(input("enter the principal amount given/taken:"))
rate=float(input("enter the rate of interest given/taken:"))
time=float(input("enter period of time(years):"))
simple_interest=principal*rate*time/100
print(f"the total amount including capital with interest :{simple_interest+principal}")
'''output:
enter the principal amount given/taken:10000
enter the rate of interest given/taken:5
enter period of time(years):1
the total amount including capital with interest :10500.0'''


#<Q5>write a python program to concatenate two strings and display the result.the strings should be taken as input from the user.
mentor_name= input()
academy_name=input()
print(mentor_name+academy_name)
'''output:
vasu garu
from pythonlife'''


#<Q6>write a program to convert a distance from kilomenters to miles.
kilometers= float(input("enter kilomters:"))
miles=kilometers*0.6
print(f"distance --->{kilometers}km={miles}mi")