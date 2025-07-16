with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

grades = [int(line.strip().split(",")[1]) for line in lines]
count_5 = grades.count(5)
print("Bahosi 5 bo‘lganlar soni:", count_5)
