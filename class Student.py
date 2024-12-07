"""
Student Details
You are given a class Student having attributes as name and age and a display method. Here, an object of student class with given name and age is created. This code uses display method to print information of the Student.

Task
Complete the given code to print the output.

Input Format
The first line of input contains name and age of Student.

Output Format
Use display method to print the name and age of Student.

Sample 1:
Input
Alice 45
Output
Alice 45
"""

class Student:
    def __init__(self, name, age): # Constructor
        #Constructor Argument
        self.name = name  # Initialize with the passed name
        self.age = age    # Initialize with the passed age

    def display(self):
        print(f"{self.name} {self.age}")

# Taking input handling for name and age
name, age = input("Enter name and age: ").split()
age = int(age)  # Convert age to an integer

# Creating a Student object with the input values
s = Student(name, age)

# Displaying the student details
s.display()


#Or Updated By CodeChef same code but no feedback in VS code, only colab gives the feedback
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0

    def display(self):
        print(f"{self.name} {self.age}")


s = Student()
s.name, s.age = input().split()

s.display()