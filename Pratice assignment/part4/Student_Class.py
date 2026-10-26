class Student:

    def __init__(self, name, roll_number, marks):

        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):

        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

    def check_result(self):

        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Rahul", 101, 75)
student2 = Student("Anjali", 102, 35)
student3 = Student("Priya", 103, 90)

students = [student1, student2, student3]

for student in students:

    student.display_details()
    print("Result:", student.check_result())
    print()