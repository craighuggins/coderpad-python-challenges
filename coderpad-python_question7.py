# Q7:
# Write a function two_sum(nums, target) that returns the indices of the two numbers in the list that add up to the target.

# Example:

# nums = [2, 7, 11, 15], target = 9  
# → return (0, 1)


# Constraints:

# Return any valid pair of indices
# Assume exactly one valid solution exists
# Time complexity O(n) is preferred, but O(n²) is acceptable if you explain it


def two_sums(nums, target): 
    for i in range(0, len(nums)): 
        for j in range(i+1, len(nums)): 
            if (nums[i] + nums[j]) == target:
                print(tuple([i, j]))
                return tuple([i, j])
            

nums = [2, 7, 11, 15]
target = 9

two_sums(nums, target)



# Optimal O(n) solution

def two_sums_2(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i


two_sums_2(nums, target)