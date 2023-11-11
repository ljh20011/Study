def sol(s, k):
    ans = 0
    for text in k:
        if text in s:
            ans += 1
    return ans

n, m = map(int, input().split())
s = []
k = []
for i in range(n):
    s.append(input())
for i in range(m):
    k.append(input())

print(sol(s, k))
