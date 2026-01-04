# Q5:
# Write a function first_non_repeating_char(s) that returns the first character in a string that does not repeat.
# If all characters repeat, return None.

# first_non_repeating_char("swiss")  → "w"
# first_non_repeating_char("aabb")   → None


# Answer:
def first_non_repeating_char(s):
    for letter in s:
        if s.count(letter) == 1:
            print(letter)
            return letter
    print(None)
    return None

first_non_repeating_char("swiss")
first_non_repeating_char("aabb")