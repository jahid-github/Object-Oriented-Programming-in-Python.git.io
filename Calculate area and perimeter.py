"""
Calculate area and perimeter
Write a class Rectangle with length and breadth as attribute and area and perimeter as methods. Given length and breadth as input, Print area and perimeter of rectangle using area and perimeter methods respectively.

Task
Complete the given code to print the area and perimeter of rectangle.

Input Format
The first line of input contains length of rectangle.
The second line of input contains breadth of rectangle.
Output Format
First line contains the output of area method of Rectangle.
Second line contains the output of perimeter method of Rectangle.
Sample 1:
Input
2 
3
Output
6
10
"""
class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def area(self):
        print(self.length * self.breadth)

    def perimeter(self):
        print(2 * (self.length + self.breadth))

r = Rectangle()

r.length = int(input())
r.breadth = int(input())

r.area()
r.perimeter()
