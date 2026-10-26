def calculate_grade (avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else :
        return "F"
students = [
    {
        "id": 101,
        "name":"Rahul",
        "python":85,
        "sql" : 75,
        "ai" : 80
    },
    {
        "id":102,
        "name":"Anjali",
        "python":60,
        "sql": 65,
        "ai": 70
    },
    {
        "id":103,
        "name":"Priya",
        "python":90,
        "sql": 85,
        "ai": 80
    },
    {
        "id":104,
        "name":"John",
        "python": 30,
        "sql": 35,
        "ai": 40
    }
]

print("==== Student Result ====")
highest_student = None
highest_average = 0

for student in students:
    total = student ["python"] + student["sql"] + student["ai"]
    average = total / 3
    grade = calculate_grade(average)

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\nStudent ID:", student["id"])
    print("Name:", student["name"])
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Result:", result)

    if average > highest_average:
        highest_average = average
        highest_student = student["name"]

students_above_75 = [
    student ["name"]
    for student in students
    if (student["python"] + student["sql"]+ student["ai"]) / 3 >75
] 

print("\nHighest Scoring Student:", highest_student)
print("Students above 75:", ",".join(students_above_75))