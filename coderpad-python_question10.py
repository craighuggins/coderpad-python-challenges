# Q10:
# Explain the difference between *args and **kwargs in Python functions.
# Provide an example where you use both in the same function.

# *args accepts any number of positional arguments in a function and are collected into a tuple, whereas **kwargs accepts any number of keyword arguments and are collected in a dictionary in the function 
# Example: 
def combined_function(arg1, *args, **kwargs): 
    print("First argument:", arg1) 
    print("Positional arguments:", args) 
    print("Keyword arguments:", kwargs) 
    
combined_function("first", 1, 2, 3, name="Craig", age=34)