with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

with open("high_scores.csv", "w") as output:
    for line in lines:
        name, grade = line.strip().split(",")
        if int(grade) == 5:
            output.write(f"{name},{grade}\n")

print("'high_scores.csv' fayliga 5 olganlar yozildi.")
