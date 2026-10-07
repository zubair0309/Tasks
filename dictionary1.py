#Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
my_dict["city"]="west godavari"
print(my_dict)

#Write Python code to access and print the value associated with the key 'price' in the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info.get('price'))

"""Write Python code to remove the key-value pair with the key 'city' from the 
following dictionary:"""
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
del my_dict['city']
print(my_dict)

#Write Python code to print all the keys present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())

#Write Python code to print all the values present in the following dictionary
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())

#Write a Python script that updates a dictionary with a new key-value pair.
dict={"a":"mani","b":"teja"}
dict["c"]="madhavi"
print(dict)
"""Write a Python script that accesses and prints the value associated with a specific 
key in a dictionary."""
print(dict.get("b"))
#Write a Python script that removes a key-value pair from a dictionary.
del dict['a']
print(dict)
#Write a Python script that prints all the keys present in a dictionary
print(dict.keys())
#Write a Python script that prints all the values present in a dictionary.
print(dict.values())