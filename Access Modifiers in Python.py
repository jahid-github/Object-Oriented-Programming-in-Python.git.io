"""
Access Modifiers in Python
In Python, access modifiers are used to control the visibility and accessibility of attributes and methods within a class. Python does not have explicit keywords like "public," "private," or "protected". Instead, It relies on naming conventions to indicate the intended visibility like-

Public: By default, all attributes and methods in a class are considered public. They can be accessed and modified from outside the class.

Protected: Attributes and methods intended for internal use within the class and its subclasses are often marked as protected by prefixing them with a single underscore (_).

Private: Attributes and methods that should not be accessed from outside the class are conventionally marked as private by prefixing them with a double underscore (__).

Task
Which of the following is a valid reason for error in the given code ?
"""
class Student:
    __age = None
    def __init__(self,age):
        self.__age = age

# Creating object of Student class
s = Student(20)
print(s.__age)

"""
Correct Answer:
age is private thus cannot be accessed directly
Explanation:
The error is due to the fact that the age field in the Student class is declared as
private. This means that it should not be accessed from outside the class.
"""