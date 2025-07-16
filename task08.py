with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

data = [line.strip().split(",") for line in lines]
grades = [int(grade) for _, grade in data]
average = sum(grades) / len(grades)
above_avg = [name for name, grade in data if int(grade) > average]

print("O‘rtachadan yuqori olganlar:")
for name in above_avg:
    print(name)
