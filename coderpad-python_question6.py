# Q6:
# Explain the difference between:

# == (equality operator)

# is (identity operator)

# Give one example where == is True but is is False.


# Answer:
# '==' checks if the values of the variable on the left and variable on the right are the same
#  'is' checks if the variable on the left and variable on the right point to the same object in memory 
# For example 
# b = [1, 2] 
# c = [1, 2] 
# "return (c is b)" would return False, whereas "return (c == b)" would return True