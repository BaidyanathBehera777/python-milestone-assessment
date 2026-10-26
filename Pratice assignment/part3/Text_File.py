with open("notes.txt", "w") as file:

    file.write("Python\n")
    file.write("SQL\n")
    file.write("AI\n")
    file.write("Playwright\n")
    file.write("Testing\n")

with open("notes.txt", "r") as file:

    lines = file.readlines()

print("Complete File")

for line in lines:
    print(line.strip())

print("\nThird Line:")
print(lines[2].strip())

with open("notes.txt", "a") as file:

    file.write("Automation Testing\n")