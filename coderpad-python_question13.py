# Q13:
# Given a string, determine whether it is a palindrome, ignoring case and non-alphanumeric characters.

# For example:

# "A man, a plan, a canal: Panama" → True  
# "hello" → False


# Write a function is_palindrome(s) to solve this.


def is_palindrome(s): 
    char_list = [char.lower() for char in s if char.isalnum()] 
    reversed_list = list(reversed(char_list)) 
    result = char_list == reversed_list 
    print(result)
    return result

is_palindrome("A man, a plan, a canal: Panama")
is_palindrome("hello")