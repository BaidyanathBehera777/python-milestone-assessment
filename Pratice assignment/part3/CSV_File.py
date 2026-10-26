import csv

with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id", "name", "salary"])
    writer.writerow([101, "Rahul", 50000])
    writer.writerow([102, "Anjali", 45000])
    writer.writerow([103, "John", 60000])

print("CSV file created successfully")