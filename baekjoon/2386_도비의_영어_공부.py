def sol(t):
    cnt = 0
    t = t.lower()
    for i in range(1, len(t)):
        if t[i] == t[0]:
            cnt += 1
    print(t[0], cnt)
    return
while(1):
    t = input()
    if t == "#":
        break
    sol(t)