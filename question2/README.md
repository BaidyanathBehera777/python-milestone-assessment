Employee File Management System
Problem Statement
Develop a Python application to store employee information in a file, read employee data, find employees with salary greater than 50000, identify the highest paid employee and count employees by role.

Approach / Logic Used
Create an Employee class with attributes and methods.
Store employee details in employees.txt.
Read data from the file using with open().
Display employee information.
Find employees earning more than 50000.
Find the highest paid employee.
Count employees based on their roles.
Handle file exceptions using try-except.
How to Run the Program
python main.py

Sample Input
101,Rahul,Python Developer,50000

102,Anjali,Tester,45000

103,John,Developer,60000

104,Priya,Tester,48000

Sample Output
===== Employee Details =====

101 - Rahul - Python Developer - $50000

102 - Anjali - Tester - $45000

103 - John - Developer - $60000

104 - Priya - Tester - $48000

===== Employees with Salary > 50000 =====

John - $60000

Highest Paid Employee:

John - $60000

Employee Count by Role:

Python Developer: 1

Tester: 2

Developer: 1

Python Concepts Used
Classes and Objects
Constructor (init)
Methods
Functions
File Handling
Context Manager (with open())
Exception Handling
Lists
Dictionaries
Loops and Conditions