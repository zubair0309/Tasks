# 1) What is the purpose of the 
# map() function in Python?
# a) To filter elements from an iterable
# b) To apply a function to each element of an iterable
# c) To reduce an iterable to a single value
# d) To sort elements of an iterable

#correct answer:b
# 2)Which of the following functions is NOT a part of the 
# a) map()
# b) filter()
# c) reduce()
# d) partial()

#correct answer:a and b

# 3) What does the filter() function do?
# a) Applies a function to each element of an iterable
# b) Reduces an iterable to a single value
# c) Filters elements from an iterable based on a condition(function returns True)
# d) Sorts elements of an iterable

#correct answer:c

# 4) In Python, what is the purpose of the reduce() function?
# a) To apply a function to each element of an iterable
# b) To filter elements from an iterable
# c) To concatenate strings or join lists
# d) To apply a function to pairs of elements in an iterable until it's reduced to a single value

#correct answer:d


# Coding exercises:
# Write a Python function 
# square_all(numbers) that takes a list of numbers as input 
# and returns a new list containing the square of each number in the input list. 
# Use the map() function with a lambda function to implement this.

def square_all(numbers):
    return list(map(lambda x: x**2, numbers))

# Example usage:
nums = [1, 2, 3, 4, 5]
print(square_all(nums))
# Output: [1, 4, 9, 16, 25]


# Write a Python function filter_positive(numbers) that takes a list of numbers as 
# input and returns a new list containing only the positive numbers from the 
# input list. Use the filter() function with a lambda function to implement this.

def filter_positive(numbers):
    return list(filter(lambda x: x > 0, numbers))

# Example usage:
nums = [-5, 3, -1, 10, 0, 7, -2]
print(filter_positive(nums))
# Output: [3, 10, 7]


# Write a Python function calculate_factorial(n) that calculates the factorial of a 
# given number n. Use the reduce() function with an appropriate lambda function to implement this

from functools import reduce

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage:
print(calculate_factorial(5))
# Output: 120

#Write a Python function count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. Use the 
# reduce() function with an appropriate lambda function to implement this.

from functools import reduce

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return reduce(lambda count, char: count + (1 if char in vowels else 0), string, 0)

# Example usage:
text = "Hello World"
print(count_vowels(text))
# Output: 3