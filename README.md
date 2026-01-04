# My CoderPad Challenge Solutions

## Question 1
In Python, what is the difference between a list, a tuple, and a set?
Please include:
- Mutability
- Ordering
- Whether duplicates are allowed
- Typical use cases


## Question 2
Write a Python function is_anagram(s1, s2) that returns True if two strings are anagrams of each other, and False otherwise.
Ignore spaces and letter case.


## Question 3
Explain how Python’s list comprehension works and rewrite the following code using a list comprehension:
```
result = []
for x in range(10):
    if x % 2 == 0:
    result.append(x * x)
```
Your answer should include:
- What list comprehensions are
- The rewritten one-liner version


## Question 4
You are given a list of words.
Write a function count_words(words) that returns a dictionary mapping each word to the number of times it appears.

### Example:
`count_words(["apple", "banana", "apple"])`
-> {"apple": 2, "banana": 1}


## Question 5
Write a function first_non_repeating_char(s) that returns the first character in a string that does not repeat.
If all characters repeat, return None.

`first_non_repeating_char("swiss")`  → "w"  
`first_non_repeating_char("aabb")`   → None


## Question 6
Explain the difference between:

== (equality operator)  
is (identity operator)

Give one example where `==` is True but `is` is False.


## Question 7
Write a function `two_sum(nums, target)` that returns the indices of the two numbers in the list that add up to the target.

### Example:
nums = [2, 7, 11, 15], target = 9    
→ return (0, 1)

### Constraints:
- Return any valid pair of indices
- Assume exactly one valid solution exists
- Time complexity O(n) is preferred, but O(n²) is acceptable if you explain it


## Question 8
Explain how Python’s garbage collection works.  
Specifically describe:
- Reference counting
- The role of the garbage collector
- What happens in a reference cycle
- Keep your answer clear and high-level


## Question 9
Given a list of integers, write a function `remove_duplicates(nums)` that returns a new list containing the same numbers in the same order, but with duplicates removed.

### Example:
`remove_duplicates([1, 2, 1, 3, 2])`  → [1, 2, 3]

### Constraints:
- Must preserve the original order
- Should run in O(n)


## Question 10
Explain the difference between *args and **kwargs in Python functions.  
Provide an example where you use both in the same function.


## Question 11
Write a function `fizz_buzz(n)` that returns a list of numbers from 1 to n, but:
- For multiples of 3, use "Fizz"
- For multiples of 5, use "Buzz"
- For multiples of both 3 and 5, use "FizzBuzz"

### Example:
`fizz_buzz(5)` → [1, 2, "Fizz", 4, "Buzz"]


## Question 12
Explain the difference between:
- Instance methods
- Class methods
- Static methods
And provide a small class example that contains one of each.


## Question 13
Given a string, determine whether it is a palindrome, ignoring case and non-alphanumeric characters.

### Example:
`"A man, a plan, a canal: Panama"` → True  
`"hello"` → False

Write a function is_palindrome(s) to solve this.


## Question 14
You are given two lists:  
`a = [1, 2, 3, 4]`  
`b = [3, 4, 5, 6]`

Write a function `list_intersection(a, b)` that returns the common elements between the two lists.

### Requirements:
- The result should contain no duplicates
- Order does not matter
- Time complexity O(n) or O(n + m) is preferred

### Example output:
[3, 4]


## Question 15
Explain what a generator is in Python, why it's useful, and write a simple generator function `count_up_to(n)` that yields numbers from 1 to n.


## Question 16
Explain the difference between:
- try / except
- try / except / finally
- try / except / else

Then provide a short example demonstrating when you would use **else** and when you would use **finally**.


## Question 17
What is inheritance in Python?
Explain it briefly and provide a simple example with:
- A base class 'Animal'
- A subclass 'Dog' that inherits from 'Animal'
