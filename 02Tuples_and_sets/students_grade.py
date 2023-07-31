intro = int(input())
stud_grades = {}
for _ in range(intro):
    entry = input().split(" ")
    student = entry[0]
    grade = entry[1]
    if student not in stud_grades:
        stud_grades[student] = []
    stud_grades[student].append(float(grade))

for student, grades in stud_grades.items():
    grades_list = " ".join(str(f"{grade:.2f}") for grade in grades)
    average = sum(grades) / len(grades)
    print(f"{student} -> {grades_list} (avg: {average:.2f})")
