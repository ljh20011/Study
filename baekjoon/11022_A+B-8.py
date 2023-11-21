def sol(a, b, i):
    print(f"Case #{i}: {a} + {b} = {a+b}")
    return

n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    sol(a, b, i)