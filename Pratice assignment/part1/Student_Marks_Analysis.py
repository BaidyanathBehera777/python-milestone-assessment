students = {
    "Rahul": 75,
    "Anjali": 35,
    "Priya": 90
}

for name, marks in students.items():

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(name, "-", result)