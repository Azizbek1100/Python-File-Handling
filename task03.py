from collections import Counter

with open("Input/grades.csv") as file:
    lines = file.readlines()[1:]  # Birinchi qator — sarlavha

# 🔹 Ma’lumotlarni ajratish
data = [line.strip().split(",") for line in lines]
grades = [int(grade) for _, grade in data]

# 19. Barcha o‘quvchilar ismi va bahosini ekranga chiqarish
print("19. O‘quvchilar va baholari:")
for name, grade in data:
    print(f"{name} - {grade}")

# 20. Baholarning o‘rtachasini hisoblash
average = sum(grades) / len(grades)
print(f"\n20. Baholarning o‘rtachasi: {round(average, 2)}")

# 21. Eng yuqori baho olgan o‘quvchini topish
top_student = max(data, key=lambda x: int(x[1]))
print(f"\n21. Eng yuqori baho olgan o‘quvchi: {top_student[0]}")

# 22. Bahosi 5 bo‘lganlar soni
count_5 = grades.count(5)
print(f"\n22. Bahosi 5 bo‘lganlar soni: {count_5}")

# 23. Har bir bahoning nechi marta qatnashgani (Counter)
grade_counts = Counter(grades)
print("\n23. Baholar nechi marta qatnashgan:")
for grade, count in grade_counts.items():
    print(f"{grade} → {count} marta")

# 24. O‘rtachadan yuqori baho olganlar
above_avg = [name for name, grade in data if int(grade) > average]
print("\n24. O‘rtachadan yuqori olganlar:")
for name in above_avg:
    print(name)

# 25. Bahosi 5 olganlarni 'high_scores.csv' fayliga yozish
with open("high_scores.csv", "w") as output:
    for name, grade in data:
        if int(grade) == 5:
            output.write(f"{name},{grade}\n")
print("\n25. ✅ 'high_scores.csv' fayliga 5 olganlar muvaffaqiyatli yozildi.")
