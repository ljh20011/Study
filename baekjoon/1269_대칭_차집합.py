def sol(a, b):
    return len((a|b) - (b&a))

n, m = map(int, input().split())

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

print(sol(a, b))
