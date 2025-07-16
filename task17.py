with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

a_names = [line.strip().split(",")[0] for line in lines if line.strip().startswith("A")]

with open("a_names.txt", "w") as out:
    for name in a_names:
        out.write(name + "\n")

print("'a_names.txt' fayliga A bilan boshlanuvchilar yozildi.")
