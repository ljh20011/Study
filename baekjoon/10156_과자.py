def sol(k, n, m):
    ans = k * n - m
    if ans < 0:
        ans = 0
    return ans

k, n, m = map(int, input().split())
print(sol(k, n, m))