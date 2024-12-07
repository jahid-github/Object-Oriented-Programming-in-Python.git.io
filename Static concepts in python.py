
#Static concepts in python
#In Python, the concept of "static" is not as explicit as in some other programming languages like Java. However, you can achieve similar functionality using class attributes and methods. Here's how you can simulate static variables, static methods, and a form of static nested class in Python:
#Static Variables (Class Attributes):
#In Python, you can use class attributes to simulate static variables shared among all instances of a class.


class MyClass:
    static_variable = 0

    def __init__(self, value):
        self.value = value
        MyClass.static_variable += 1

# Accessing the static variable
print(MyClass.static_variable)


#In this example, static_variable is a class attribute shared by all instances of MyClass.
#Static Methods:
#You can use the @staticmethod decorator to define static methods that don't require access to the instance.

class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")
# Calling the static method
MyClass.static_method()
#Static methods do not have access to instance-specific data and are called on the class rather than an instance.
