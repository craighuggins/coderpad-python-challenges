# Q4:
# You are given a list of words.
# Write a function count_words(words) that returns a dictionary mapping each word to the number of times it appears.

# Example:

# count_words(["apple", "banana", "apple"])
# # -> {"apple": 2, "banana": 1}


# Write the function as you would in a live coding interview.


def count_words(input_list: list): 
    new_dict = {} 
    for item in input_list: 
        new_dict.update({item:input_list.count(item)})  # This is O(n), and you do it for every item in the list, making the entire solution O(n²).
    print(new_dict)
    return new_dict



count_words(["apple", "banana", "apple"])


# Better solution that is O(n) implementation
def count_words_2(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    print(counts)
    return counts

count_words_2(["apple", "banana", "apple"])