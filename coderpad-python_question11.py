# Q11:
# Write a function fizz_buzz(n) that returns a list of numbers from 1 to n, but:

# For multiples of 3, use "Fizz"

# For multiples of 5, use "Buzz"

# For multiples of both 3 and 5, use "FizzBuzz"

# Example:
# fizz_buzz(5) → [1, 2, "Fizz", 4, "Buzz"]

def fizz_buzz(n): 
    new_list = [] 
    for i in range(1, n + 1): 
        if i % 3 == 0: 
            if i % 5 == 0: 
                val = "FizzBuzz" 
            else: 
                val = "Fizz" 
        elif i % 5 == 0: 
            val = "Buzz" 
        else: 
            val = i 
        new_list.append(val) 
        
    print(new_list)
    return new_list

fizz_buzz(20)