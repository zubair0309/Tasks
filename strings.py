# Question 1:
# What is the main characteristic of Python strings?
# a) Mutable
# b) Immutable
# c) Dynamic
# d) Static
#correct answer:b

# Question 2:
# How can you access the last character of a string in Python?
# a) my_string[-1]
# b) my_string[last]
# c) my_string[last_char]
# d) my_string(end)
#correct answer:a

# Question 3:
# Which method is used to convert a string to uppercase in Python?
# a) to_upper()
# b) uppercase()
# c).upper()
# d) case_upper()
#correct answer:c

# Question 4:
# What does the split() method do?
# a) Combines strings
# b) Splits a string into a list of substrings
# c) Finds a substring in a string
# d) Converts a string to lowercase
#correct answer:b

# Question 5:

# Which method is used to check if a string starts with a specific prefix?
# a) startswith()
# b)startwith()
# c) beginwith()
# d) initwith()
#correct answer:a

#Coding Exercise 
#1 Problem:
#You are given a string sentence . Print the characters at even indices.

sentence = "Python is amazing"
even_index_chars = sentence[::2]
print(even_index_chars)

# output:Pto saaig

#2 Problem:
#You are given a string s . Replace all spaces in the string with underscores (_)and print the modified string.

s = "Python is fun and powerful"
modified_s = s.replace(" ", "_")
print(modified_s)

# output:Python_is_fun_and_powerful

# 3 Problem:
#You are given a string s . Check if the string contains only digits

s = "12345"
is_only_digits = s.isdigit()
print(is_only_digits)

# output:True

#4 Problem:
#You are given a string s . Print the string in reverse order.

s = "Python is amazing"
reversed_s = s[::-1]
print(reversed_s)

# output:gnizama si nohtyP

#Problem:
#You are given a string s . Capitalize the first letter of each word in the string and print the modified string
s = "python programming is fun"
title_s = s.title()
print(title_s)

#output:"Python Programming Is Fun"