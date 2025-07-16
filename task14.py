with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

names = [line.strip().split(",")[0] for line in lines]

with open("names_only.csv", "w") as out:
    for name in names:
        out.write(name + "\n")

print("'names_only.csv' fayliga ismlar yozildi.")
