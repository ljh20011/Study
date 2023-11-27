def sol(point, grade):
    return grade / point


all_point = 0
grade = 0

for i in range(20):
    temp = list(input().split())
    if temp[2] == ("P"):
        continue
    all_point += float(temp[1])
    point = float(temp[1])
    if temp[2] == "A+":
        grade += 4.5 * point
    if temp[2] == "A0":
        grade += 4.0 * point
    if temp[2] == "B+":
        grade += 3.5 * point
    if temp[2] == "B0":
        grade += 3.0 * point
    if temp[2] == "C+":
        grade += 2.5 * point
    if temp[2] == "C0":
        grade += 2.0 * point
    if temp[2] == "D+":
        grade += 1.5 * point
    if temp[2] == "D0":
        grade += 1.0 * point
    else :
        grade += 0

print(sol(all_point,grade))