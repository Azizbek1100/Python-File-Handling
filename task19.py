with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

for line in lines:
    name, grade = line.strip().split(",")
    print(f"{name} - {grade}")
