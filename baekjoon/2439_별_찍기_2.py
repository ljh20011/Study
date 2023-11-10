def sol(n):
    for i in range(1, n+1):
        print((n - i) * " ",end ="")
        print(i * "*")

# n = map(int, input().split())
n = int(input())
sol(n)