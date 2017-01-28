

n = int(input())
marks = 0
for i in range(n):
    grade = int(input())
    rem = grade % 5
    if grade < 38:
        marks = grade
    elif rem >= 3:
        marks = grade - rem + 5
    else:
        marks = grade
    print(marks)