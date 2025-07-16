# 4-misol: Baholarning o‘rtachasini hisoblash

with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

grades = [int(line.strip().split(",")[1]) for line in lines]
average = sum(grades) / len(grades)
print("Baholarning o‘rtachasi:", round(average, 2))
