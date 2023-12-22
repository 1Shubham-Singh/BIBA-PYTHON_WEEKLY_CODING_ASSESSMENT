# 1.Explain Python Module with examples

# A module is a file containing Python code, 
# definitions of functions, statements, or classes. An example_module.py file is a module
# we will create and whose name is example_module. We employ modules to divide complicated programs into smaller, 
# more understandable pieces. Modules also allow for the reuse of code.
# a.Import module in Python
# .Renaming the Python module
 
#importing And Renaming

import math as m
print(m.sqrt(25))

import cal as c
print(c.add(20,30))

# Example using the sys module
import sys
print(sys.version)
print(sys.argv)

#Exmples using json 
import json
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
json_data = json.dumps(data)
print(json_data)

# User defined module
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b
import cal as c

print("Addition of 5 and 4 is:", c.add(5, 4))
print("Subtraction of 7 and 2 is:", c.sub(7, 2))

