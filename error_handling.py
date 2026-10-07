# ZeroDivisionError
try:
     a = 10
     b = 0
     result = a / b
     print(result)
  except ZeroDivisionError:
     print("Error: Division by zero is not allowed.")


    #output:Error: Division by zero is not allowed.

#ValueError Handling
 try:
    user_input = "abc"
    number = int(user_input)
     print(number)
 except ValueError:
     print("Error: Invalid literal for int conversion.")

# output:Error: Invalid literal for int conversion.

#IndexError Handling

 try:
     items = [10, 20, 30]
     element = items[5]
     print(element)
 except IndexError:
    print("Error: List index out of range.")
         
# output:Error: List index out of range.

#KeyError Handling

 try:
     student = {"name": "Alex", "age": 20}
     grade = student["grade"]
     print(grade)
 except KeyError:
     print("Error: Key not found in dictionary.")

# output:Error: Key not found in dictionary.

#FileNotFoundError Handling

 try:
     file = open("non_existent_file.txt", "r")
     content = file.read()
     file.close()
 except FileNotFoundError:
     print("Error: The requested file does not exist.")

# output:Error: The requested file does not exist.


#TypeError Handling

 try:
     text = "Score: "
     score = 95
     output = text + score
     print(output)
 except TypeError:
     print("Error: Unsupported operand types for concatenation.")

# output:Error: Unsupported operand types for concatenation.

#AttributeError Handling

 try:
     number = 42
     number.append(5)
 except AttributeError:
     print("Error: Object has no such attribute or method.")

# output:Error: Object has no such attribute or method.


#OverflowError Handling
# import math

 try:
     result = math.exp(1000)
     print(result)
 except OverflowError:
     print("Error: Math result is too large to represent.")

# output:Error: Math result is too large to represent.

#IOError
 try:
     file = open("/root/protected_file.txt", "w")
     file.write("Data")
     file.close()
 except IOError:
     print("Error: Input/Output operation failed.")

# output:Error: Input/Output operation failed.

#RuntimeError 
 try:
    raise RuntimeError("A generic system or execution failure occurred.")
 except RuntimeError as error:
     print(f"Error caught: {error}")
# output:Error caught: A generic system or execution failure occurred.

#Exception 
try:
    num = 10
    result = num + "apple"
    print(result)
except Exception as error:
    print(f"Error caught: {error}")

#output:Error caught: unsupported operand type(s) for +: 'int' and 'str'