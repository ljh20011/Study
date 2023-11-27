def sol(n):
    chk = [0] * 10
    for i in range(len(n)):
        if int(n[i]) == 9:
            chk[6] += 1
        else:
            chk[int(n[i])] += 1
    if chk[6] % 2 == 0:
        chk[6] = chk[6] // 2
    else :
        chk[6] = (chk[6] // 2) + 1
    return max(chk)

n = input()
print(sol(n))