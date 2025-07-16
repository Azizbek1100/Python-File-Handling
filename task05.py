with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

data = [line.strip().split(",") for line in lines]
top_student = max(data, key=lambda x: int(x[1]))
print("Eng yuqori baho olgan:", top_student[0])
