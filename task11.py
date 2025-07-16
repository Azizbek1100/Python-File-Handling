with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

for line in lines:
    name, grade = line.strip().split(",")
    if name.startswith("A"):
        print(f"{name} - {grade}")
