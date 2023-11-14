def sol(hear, look):
    hear = set(hear)
    look = set(look)

    ans = list(hear & look)
    ans.sort()
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])
    return

n, m = map(int, input().split())
hear = []
look = []

for i in range(n):
    hear.append(input())
for i in range(m):
    look.append(input())

sol(hear, look)
