# Structure of a function
"""
def function_name(parameters):
    # Function body (code block)
    # ...
    return result  # Optional return statement

def: Keyword to define a function.
function_name: Name of the function (should be descriptive).
parameters: Inputs that the function accepts (can be optional).
Function body: Code block where the function performs its task.
return: Optional statement to return a value from the function.
"""

# example of using function to print out (a + b) ^ 2 and a + b
def compute_value(a, b):
    local = a ** 2 + 2 * a * b + b ** 2
    regular = a + b
    print (local)
    print (regular)

compute_value(3, 5)
