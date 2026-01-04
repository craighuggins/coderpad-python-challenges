# Q17:
# What is inheritance in Python?
# Explain it briefly and provide a simple example with:

# A base class Animal

# A subclass Dog that inherits from Animal


# Answer:
# Inheritance allows one class to inherit all the methods and properties of another 'Parent' class

class Animal:
    def __init__(self, size, age):
        self.size = size
        self.age = age

    def show_size(self):
        print("Size: ", self.size)

    def show_age(self):
        print("Age: ", self.age)

class Dog(Animal):
    # Dog inherits the methods and properties of an animal
    def bark(self):
        print("Woof!")


new_animal = Animal("large", 3)
new_animal.show_size()

new_dog = Dog("small", 8)
new_dog.show_size()
new_dog.bark()