# Q3:
# Explain how Python’s list comprehension works and rewrite the following code using a list comprehension:

# result = []
# for x in range(10):
#     if x % 2 == 0:
#         result.append(x * x)


# Your answer should include:

# What list comprehensions are

# The rewritten one-liner version



# Answer:
# List comprehension works by creating a list variable, and inside that list contains an expression that is to be performed for each element in an iterable object. 
# There is an optional conditional statement at the end
# The rewritten code is: 

result = [x*x for x in range(10) if x % 2 == 0]