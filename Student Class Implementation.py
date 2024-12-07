
"""
Student Class Implementation
You are given a Student class having name and age as attributes and a display method. This class also has a parameterized constructor having name and age as parameters to initialize the value of name and age of student respectively.
Given name and age as input, Create a student class, initialize the values and then print the information of Student using display method.

Input Format
First line contain a string representing name of the student.
Second line contain a integer representing age of the student.
Output Format
Print the information of the student using display method.

Sample 1:
Input
Alice 
12
Output
Alice 
12
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

name = input()
age = int(input())
#or
#name,age = input().split()
#age = int(age)

obj = Student(name, age)
obj.display()
