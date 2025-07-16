with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

print("Ismi 5 harfdan uzun bo‘lgan talabalar:")
for line in lines:
    name, _ = line.strip().split(",")
    if len(name) > 5:
        print(name)
