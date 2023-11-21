def sol(a):
    a.sort()
    return a[1]

a = list(map(int, input().split()))
print(sol(a))