def sol(n, member):
    cnt = 1
    idx = 0
    while len(member) > 1:
        idx = ((idx-1) +(cnt**3) )% len(member)# 날릴 원소, 다음번에 시작할 원소
        member.pop(idx)
        cnt += 1
    print(*member)
    return
n = int(input())
member = list(range(1,n+1))
sol(n, member)