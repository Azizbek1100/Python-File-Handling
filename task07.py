from collections import Counter

with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

grades = [int(line.strip().split(",")[1]) for line in lines]
grade_counts = Counter(grades)

print("Baholar nechi marta qatnashgan:")
for grade, count in grade_counts.items():
    print(f"{grade} → {count} marta")
