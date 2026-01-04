# Q8:
# Explain how Python’s garbage collection works.
# Specifically describe:

# Reference counting

# The role of the garbage collector

# What happens in a reference cycle

# Keep your answer clear and high-level, as if in a real interview.


# Answer:
# Python manages garbage collection automatically. 
# Reference counting refers to each object having a count of how many references there are to it in the program. 
# When the count reaches 0, the object is recycled and the memory it used is freed up. 
# The garbage collector ensures that no memory exhaustion or memory leaks occur

# Polished Answer:
# Here is the answer you should give in an interview:

# Python uses automatic memory management based on two systems: reference counting and a cyclic garbage collector.

# 1. Reference Counting:
# Every Python object keeps track of how many references point to it. When this count reaches zero—meaning nothing references it—the object is immediately destroyed and its memory is freed.

# 2. Garbage Collector (GC):
# Reference counting can’t handle reference cycles, where two or more objects reference each other. Even if they are unreachable from the program, their reference counts never reach zero.

# 3. Reference Cycles:
# Python’s GC periodically scans for groups of objects that reference each other but are no longer reachable from the program. It detects these cycles and frees them even though their reference counts are non-zero.

# So reference counting handles most objects immediately, and the GC handles cycles.