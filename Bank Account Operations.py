"""
Bank Account Operations
This code demonstrates a basic implementation of a bank account system using object-oriented programming (OOP) principles in Python. Here's an explanation of the code:

BankAccount Class:

This class represents a bank account.
It has three private attributes: accountNumber, accountHolder and balance
The class includes a constructor to initialize the attributes when creating a new account.
Deposit Method (deposit): This method allows you to deposit a specified amount into the account.

Withdraw Method (withdraw): This method allows you to withdraw a specified amount from the account.

Get Account Information Method (getAccountInfo):

This method displays the account information, including the account number, account holder's name, and the current balance.
Task
Create an instance of the BankAccount class named account with an initial account number = 12345 and account holder's name = John Doe. Perform deposit of 1000, withdrawal of 500 and deposit of 200. Finally, display the account information using the getAccountInfo method.

This code simulates a simple bank account system where you can create an account, deposit and withdraw funds, and view the account details.

Sample 1:
Input:
Output:
Deposited: $1000
Withdrawn: $500
Deposited: $200
Account Number: 12345
Account Holder: John Doe
Balance: $700
"""
class BankAccount :
    __accountNumber = None
    __accountHolder = None
    __balance = None
    
    def __init__(self, accountNumber, accountHolder): 
        BankAccount.__accountNumber = accountNumber
        BankAccount.__accountHolder = accountHolder
        BankAccount.__balance = 0
    
    def deposit(self , value): 
        BankAccount.__balance += value
        print(f"Deposited: ${value}")
        
    def withdraw(self , value): 
        BankAccount.__balance -= value
        print(f"Withdrawn: ${value}")

    def getAccountInfo(self):
        print(f"Account Number: {BankAccount.__accountNumber}");
        print(f"Account Holder: {BankAccount.__accountHolder}");
        print(f"Balance: ${BankAccount.__balance}"); 


# Create a BankAccount object
account = BankAccount(12345, "John Doe");

# Perform deposits and withdrawals and display account info
account.deposit(1000);
account.withdraw(500);
account.deposit(200);

# Display the final account information
account.getAccountInfo();

"""
BankAccount_Explanation
https://docs.google.com/document/d/1TYERRz7JekcUXg5ZzcbHRx8syN9R6HRf/edit?usp=drive_link&ouid=103626731674467575283&rtpof=true&sd=true
"""