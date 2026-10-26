class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = float(salary)
    def display_details(self):
        print(
            f"{self.employee_id} - {self.name} - {self.role} -${int(self.salary)}"    
        )

def add_employee():
    employees =[
        "101,Rahul,Python Developer,50000",
        "102,Anjali,Tester,45000",
        "103,John,Developer,60000",
        "104,Priya,Tester,48000"
    ]
    with open("employees.txt", "w") as file:
        for employee in employees:
            file.write(employee +"\n")

def read_employees():

    employee_list =[]

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                employee = Employee(
                    data[0],
                    data[1],
                    data[2],
                    data[3]
                )

                employee_list.append(employee)
    except FileNotFoundError:
        print("employees.txt file not found")
    return employee_list

def find_highest_salary(employee_list):
    highest = employee_list[0]

    for employee in employee_list:
        if employee.salary > highest.salary:
            highest = employee
    return highest
def find_employees_by_role(employee_list):
    role_count = {}
    for employee in employee_list:
        if employee.role in role_count:
            role_count[employee.role] +=1
        else:
            role_count[employee.role] =1
    return role_count
add_employee()
employees = read_employees()
print("==== Employee Details ====\n")
for employee in employees:
    employee.display_details()
print("\n==== Employee with Salary > 50000 ====\n")
for employee in employees:
    if employee.salary >50000:
        print(f"{employee.name} - ${int(employee.salary)}")
highest_employee = find_highest_salary(employees)
print("\nHighest Paid Employee:")
print(f"{highest_employee.name} - ${int(highest_employee.salary)}")
role_data = find_employees_by_role(employees)
print("\nEmployee Count by Role:")
for role, count in role_data.items():
    print(f"{role}: {count}")


