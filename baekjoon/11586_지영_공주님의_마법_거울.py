def sol(mirror, k, n):
    if k == 1:
        for i in mirror:
            print(i)
    if k == 2:
        for i in mirror:
            print(i[::-1])
    if k == 3:
        for i in mirror[::-1]:
            print(i)
    return

n = int(input())
mirror = []
for i in range(n):
    mirror.append(input())
k = int(input())
sol(mirror, k, n)