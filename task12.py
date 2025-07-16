with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

data = [line.strip().split(",") for line in lines]
low_student = min(data, key=lambda x: int(x[1]))
print("Eng past baho olgan:", low_student[0])
