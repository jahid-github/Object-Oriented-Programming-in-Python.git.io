"""
Accessing and Modifying Private Data Members
In Python, getter and setter methods are used to access and modify private data members (fields) of a class. Here's how you can create getter and setter methods for private data members:

Getter Method: A getter method allows you to retrieve the value of a private field.

Setter Method: A setter method allows you to modify the value of a private field.

Using Getter and Setter: You can use the getter and setter methods to access and modify the private field.

In this example, the setMyField method sets the value of myField, and the getMyField method retrieves the value. Getter and setter methods provide controlled access to private fields.
"""
class MyClass :
    __myField = None
    
    # Getter method for myField
    def getMyField(self): 
        return MyClass.__myField

    # Setter method for myField
    def setMyField(self , value): 
        MyClass.__myField = value


obj = MyClass()
# Using the setter method to set the value of myField
obj.setMyField(42)
# Using the getter method to retrieve the value of myField
value = obj.getMyField()
print("Value of myField: ", value)

"""
Code Explanation: MyClass Example
https://docs.google.com/document/d/1AghLt7gsaxO6jzJnaR1jbfp6Ap_9nJJF/edit?usp=drive_link&ouid=103626731674467575283&rtpof=true&sd=true
"""