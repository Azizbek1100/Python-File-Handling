with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

for line in lines:
    name, grade = line.strip().split(",")
    if int(grade) == 3:
        print(name)
