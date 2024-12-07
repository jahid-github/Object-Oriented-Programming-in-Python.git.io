"""
Write your first class
Writing a class in Python involves defining the structure and behavior of objects based on the principles of object-oriented programming. Here's a step-by-step guide on how to write a basic class in Python:

This code demonstrates the basic structure of a python program:

Class Definition:

In Python, a class is defined using the class keyword followed by the class name. In the example, we define a class named Person.
Constructor (__init__ method):

The __init__ method is a special method that serves as the constructor. It is called when an object of the class is created.
It initializes the instance attributes. In our example, name and age are instance attributes.
Instance Attributes:

Attributes are variables that store data related to an instance of a class.
In our example, name and age are instance attributes. Each instance of the Person class has its own values for these attributes.
Instance Methods:

Methods are functions defined within a class and operate on the instance of the class.
In our example, greet is an instance method. It takes no argument other than self, which refers to the instance of the class.
Creating Instances:

We create instances of a class by calling the class name as if it were a function. This creates a new object with its own set of attributes.
In the example, person1 and person2 are instances of the Person class.
Accessing Attributes and Calling Methods:

Once instances are created, we can access their attributes using dot notation (object.attribute).
We call methods on instances using the same dot notation (object.method()).
Self Parameter:

The self parameter in Python is a convention that represents the instance of the class. It is the first parameter in instance methods and is automatically passed when calling the method.
Understanding these concepts is crucial for working with object-oriented programming in Python. Classes and objects provide a way to structure and organize code, encapsulating data and functionality within a single unit.
"""
class Person:
    def __init__(self, name, age):  # Corrected constructor
        # Instance attributes
        self.name = name  # Assigning the name parameter
        self.age = age    # Assigning the age parameter

    def greet(self):
        # Instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Testing the greet method
person1.greet()
person2.greet()
