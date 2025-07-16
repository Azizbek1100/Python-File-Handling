# 3-misol: Barcha o‘quvchilar ismi va bahosini ekranga chiqarish

with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]  # Headerni tashlab o‘t

for line in lines:
    name, grade = line.strip().split(",")
    print(f"{name} - {grade}")
