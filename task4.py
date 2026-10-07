# 1. Variables and Data Types
a = 35
b = "pythonlife"
print(a)
print(b)
"""
output: 35
pythonlife
"""

# 2. Pattern Printing
print("   *   ")
print("  ***  ")
print(" ***** ")
print("*******")
print(" ***** ")
print("  ***  ")   
print("   *   ")
"""
output:
   * 
  ***  
 ***** 
*******
 ***** 
  ***  
   * 
"""

# 3. Data Types
a = 10
b = 3.14
c = "Hello, World!"
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
"""
output:
10
3.14
Hello, World!
<class 'int'>
<class 'float'>
<class 'str'>
"""

# 4. Data Types Identification
city_name = "New York"
population_millions = 8.4196
year_established = 1624
has_subway = True

print(city_name, "->Type:", type(city_name))          
print(population_millions, "->Type:", type(population_millions))  
print(year_established, "->Type:", type(year_established))  
print(has_subway, "->Type:", type(has_subway))      
"""
output:
New York ->Type: <class 'str'>
8.4196 ->Type: <class 'float'>
1624 ->Type: <class 'int'>
True ->Type: <class 'bool'>
"""

# 5. Object Memory ID Check
student_id = 456
person_name = "Alice"
print(id(student_id))
print(id(person_name))
"""
output:
1759569763280
1759569992112
"""

# 6. Type Conversion (Age string to int)
age_str = "25"
age_int = int(age_str)
print(age_int)
print(type(age_int))
"""
output:
25
<class 'int'>
"""

# 7. string Concatenation
a = "mahesh"
b = "kumar"
print(a + b)
"""
output:
maheshkumar
"""

# 8.Type Conversion (Number string to Int)
number_text = "100"
number_int = int(number_text)
print("Value:", number_int)
print(" DataType:", type(number_int))
"""
output:
Value: 100
 DataType: <class 'int'>
"""


      