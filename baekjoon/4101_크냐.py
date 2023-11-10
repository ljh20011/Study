def sol(a, b):
    if a > b :
        print("Yes")
    else :
        print("No")

while(1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else :
        sol(a, b)