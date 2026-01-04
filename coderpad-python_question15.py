# Q15:

# Explain what a generator is in Python, why it's useful, and write a simple generator function count_up_to(n) that yields numbers from 1 to n.



# Answer:
# generator functions are used to generate numbers on demand rather than computing and storing them in memory. 
# The 'yield' keyword is used instead of 'return'

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

gen_val = count_up_to(20)
for value in gen_val:
    print(value)