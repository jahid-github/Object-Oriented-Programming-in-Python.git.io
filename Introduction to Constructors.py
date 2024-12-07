"""
Introduction to Constructors
In Python, a constructor is a special method that gets called when an object is created. Constructors are used to initialize the attributes of an object. In Python, there are two types of constructors:

Default Constructor (or __init__ method):

The default constructor is the most common type in Python.
It is automatically called when an object is created.
It is defined using the __init__ method.
Example:
"""
class MyClass:
    def __init__(self):
        # Code

# Creating an object of MyClass
obj = MyClass()
"""
In this example, the __init__ method is the constructor that initializes the attribute1 and attribute2 of the MyClass object.

Parameterized Constructor:

A parameterized constructor allows you to pass values to the constructor when creating an object.
It allows you to initialize the attributes with the values provided during object creation.
Example:
"""
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

# Creating an object of MyClass with values
"""
obj = MyClass("value1", "value2")
In this example, the constructor takes parameters attribute1 and attribute2, and you can pass values to them when creating an object.

These are the two main types of constructors in Python. The default constructor is more common, but parameterized constructors provide more flexibility when you need to initialize the object with specific values.
"""