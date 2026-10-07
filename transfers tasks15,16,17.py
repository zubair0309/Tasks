"""Problem 1 Using 
break in a While Loop
Write a Python program that takes a list of numbers as input 
numbers = [25, 30, 
20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds 
100, stop adding numbers and print "Sum exceeded 100" """

numbers = [25, 30, 
20, 40, 15, 25]
sum_1=0
index=0
while index <len(numbers):
    sum_1+=numbers[index]
    if sum_1 >100:
        print("sum exceeds 100")
        break
    index+=1
print("total sum:",sum_1)

"""Problem 2 Using 
continue in a For Loop
Write a Python script that uses a for loop to iterate through numbers from 1 to 
600. Print only the odd numbers, skipping the even ones using the 
statement."""

for i in range(1,601):
    if i%2==0:
        continue
    print(i)

    """Write a Python script that checks if a number is even or odd. If the number is 
even, print "Even"; if odd, do nothing (use the 
pass statement)."""

numbers_1=int(input("enter the number:"))
for i in range(numbers_1):
    if i%2==0:
        print("even")
        break
    else:
        pass

    """Problem 4 Combining Transfer Statements
Write a Python script that iterates through a list of words. If the word is "break," 
exit the loop using the 
break statement. If the word is "skip," skip the rest of the 
code for the current iteration using the 
continue statement. For any other word, 
print the word."""

sample=["break","skip","list","tuple","pythonlife"]
for i in sample:
    if i=="break":
        break
for i in sample:
    if i=="skip" or i=="break":
        continue
    print(i)

    #indexing
sample=[12,13,14,15,16,78]
print(sample[3])
    #slicing
print(sample[:5:2])
print(sample[::3])
