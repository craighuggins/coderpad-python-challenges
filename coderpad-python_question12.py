# Q12:
# Explain the difference between:

# Instance methods

# Class methods

# Static methods

# And provide a small class example that contains one of each.

# Answer:
# Instance methods operate on instances of classes and receive 'self' as their first parameter. They can modify the instance's data. 
# Class methods operate on the class itself rather than the instance. They are defined using the @classmethod decorator and receive 'cls' as the first parameter. These can modify data of the class as a whole. 
# Static methods are logically related to the class but do not have access to or modify the class or instances data. They are defined within a class for structural/organisational purposes


# Example class:
class Example:
    class_count = 0

    def __init__(self, value):
        self.value = value
        Example.class_count += 1

    # Instance method
    def show_value(self):
        print(f"Instance value: {self.value}")
        return f"Instance value: {self.value}"

    # Class method
    @classmethod
    def get_instance_count(cls):
        print(f"Instances created: {cls.class_count}")
        return f"Instances created: {cls.class_count}"

    # Static method
    @staticmethod
    def is_positive(number):
        print(number > 0)
        return number > 0


e = Example(10)
f = Example(20)
e.show_value()             # Instance method
f.show_value()
Example.get_instance_count()  # Class method
Example.is_positive(5)        # Static method
