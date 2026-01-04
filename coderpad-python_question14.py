# Q14:
# You are given two lists:

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# Write a function list_intersection(a, b) that returns the common elements between the two lists.

# Requirements:
# The result should contain no duplicates
# Order does not matter
# Time complexity O(n) or O(n + m) is preferred

# Example output:
# [3, 4]


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

# def list_intersection(a, b): 
#     common = [] 
#     for item in a: 
#         if item in b: 
#             common.append(item) 
#             b.remove(item) 
#     print(common)
#     return common


# Better O(n) solutions
def list_intersection_2(a, b):
    print(list(set(a) & set(b)))
    return list(set(a) & set(b))

def list_intersection_3(a, b):
    b_set = set(b)
    print([x for x in set(a) if x in b_set])
    return [x for x in set(a) if x in b_set]


# list_intersection(a, b)
list_intersection_2(a, b)
list_intersection_3(a, b)