with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

grades = [int(line.strip().split(",")[1]) for line in lines]
total = sum(grades)
print("Baholar yig‘indisi:", total)
