def sol(a):
    for i in range(a,0,-1):
        print(" " * (a-i)+ ("*" * i))
    return

a = int(input())
sol(a)