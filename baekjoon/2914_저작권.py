def sol(a, i):
    return round(a * (i-1) + 1)

a, i = map(int, input().split())
print(sol(a, i))