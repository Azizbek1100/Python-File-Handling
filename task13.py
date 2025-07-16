with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

grades = [int(line.strip().split(",")[1]) for line in lines]
num_4 = grades.count(4)
percentage = (num_4 / len(grades)) * 100
print("Bahosi 4 bo‘lganlar foizi:", round(percentage, 1), "%")
