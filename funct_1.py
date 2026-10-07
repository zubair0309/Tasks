#additon function
def add(a,b):
    return a+b
print(add(1,4))
#square functions
def square(x):
    return x**2
print(square(45))
#factorial functions
def factorial(n):
    return (n-1)*n
n=int((input("Enter the positive integer: ")))
print(factorial(n))
#maximum functions
def maximum():
    numbers=[34,45,67,99,100,125,143]
    return max(numbers)
print(maximum())
#reverse function
def reverse(str):
    return str[::-1]
string=input("enter the string: ")
print(reverse(string))
#prime functions
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter number: "))

if prime(num):
    print("Prime")
else:
    print("Not Prime")
