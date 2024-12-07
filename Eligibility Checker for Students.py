"""
Eligibility Checker for Students
You are tasked with designing a simple program that determines the eligibility of students based on their scores and ages.

Class Definitions:

Student class:

Attributes:
name (String): The name of the student.
score (int): The student's academic score.
age (int): The age of the student.
Methods:
eligible(): A method that checks the student's eligibility and prints "YES" if the score is greater than 10 and the age is greater than 20. Otherwise, it prints "NO."
The main method:

Creates an instance of the Student class.
Sets the name, score, and age attributes for the student with predefined values.
Calls the eligible method to determine and display the student's eligibility.
Task
Write the eligible method of student class to make Eligibility Checker for Students.
"""
class Student:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.age = 0

    def eligible(self):
        # Eligibility criteria: score >= 10 and age >= 18
        if self.score >= 10 and self.age >= 18:
            return f"{self.name} is eligible."
        else:
            return f"{self.name} is not eligible."


# Example usage
obj = Student()
obj.name = "Tom"
obj.score = 15
obj.age = 21
print(obj.eligible())  # Output: Tom is eligible.

"""
Explanation

1. **Class Structure:**
   - The `Student` class has three instance variables: `name`, `score`, and `age`, initialized in the constructor.

2. **`eligible` Method:**
   - This method checks if a student meets the eligibility criteria (e.g., score >= 10 and age >= 18).
   - If the conditions are met, it returns a message indicating the student is eligible; otherwise, it states they are not eligible.

3. **Setting Attributes:**
   - The `name`, `score`, and `age` attributes are set after creating the `Student` object.

4. **Checking Eligibility:**
   - `eligible()` evaluates the conditions and returns a message accordingly.
"""

#Or CodeChef Solution
class Student:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.age = 0

    def eligible(self):
        if self.score > 10 and self.age > 20:
            print("YES")
        else:
            print("NO")

obj = Student()
obj.name = "Tom"
obj.score = 15
obj.age = 21
obj.eligible()