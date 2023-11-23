def sol(l):
    l.sort()
    print(l[-1][0])
    print(l[-1][1])
    return

l = []
for i in range(1, 10):
    temp = int(input())
    l.append([temp, i])
sol(l)

