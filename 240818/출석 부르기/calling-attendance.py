students = {1:"John", 2: "Tom", 3: "Paul"}
n = int(input(""))
if n in students.keys():
    print(students[n])
else:
    print("Vacancy")