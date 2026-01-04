# Q9:
# Given a list of integers, write a function remove_duplicates(nums) that returns a new list containing the same numbers in the same order, but with duplicates removed.

# Example:
# remove_duplicates([1, 2, 1, 3, 2]) → [1, 2, 3]


# Constraints:
# Must preserve the original order
# Should run in O(n)


def remove_duplicates(nums): 
    seen = [] 
    new_list = [] 
    for num in nums: 
        if num not in seen: 
            new_list.append(num) 
            seen.append(num)
    print(new_list)
    return new_list

remove_duplicates([1, 2, 1, 3, 2])


# Interview-Preferred O(n) Solution

# Use a set for O(1) membership tests.

# Track order with a list.

def remove_duplicates_2(nums):
    seen = set()
    new_list = []
    for num in nums:
        if num not in seen:
            new_list.append(num)
            seen.add(num)
    print(new_list)
    return new_list

remove_duplicates_2([1, 2, 1, 3, 2])