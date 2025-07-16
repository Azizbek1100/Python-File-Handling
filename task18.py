user_name = input("Ism kiriting: ").strip()

with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]

names = [line.strip().split(",")[0] for line in lines]

if user_name in names:
    print(f"{user_name} faylda mavjud ✅")
else:
    print(f"{user_name} topilmadi ❌")
