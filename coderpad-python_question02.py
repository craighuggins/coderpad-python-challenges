#  Q2:
# Write a Python function is_anagram(s1, s2) that returns True if two strings are anagrams of each other, and False otherwise.
# Ignore spaces and letter case. 




# Answer:
def is_anagram(s1, s2):
    s1 = ''.join(s1.lower().split())
    s2 = ''.join(s2.lower().split())
    print(sorted(s1) == sorted(s2))
    return sorted(s1) == sorted(s2)


is_anagram("hello", "oehll")