# Q16:
# Explain the difference between:

# try / except

# try / except / finally

# try / except / else

# Then provide a short example demonstrating when you would use else and when you would use finally.


# Answer:
# 'try / except' first runs the code in the 'try' block, and then runs the code in the 'except' block if an exception (or error) is encountered. 
# 'try / except / finally' first runs the code in the 'try' block, and then runs the code in the 'except' block if an exception (or error) is encountered, and then afterwards runs the code in the 'finally' block. The code in the 'finally' block is run regardless of whether the code in 'except' gets executed or not
# 'try / except / else' The else block runs only if no exception occurs in the try block. It is useful for code that should run only when the try succeeds, keeping it separate from the error-handling logic.

# def example():
#     try:
#         # code that might fail
#     except:
#         # error handling
#     else:
#         # runs only if try did NOT raise an exception


# Example: else
# Use else when you only want code to run if no exception happened:
def example_else():
    try:
        num = int("123")
    except ValueError:
        print("Invalid number")
    else:
        print("Conversion succeeded:", num)


# Example: finally
# Use finally for cleanup that must happen no matter what:
def example_finally():
    file = open("test.txt", "w")
    try:
        file.write("Hello")
    except Exception:
        print("Write failed")
    finally:
        file.close()  # Always runs