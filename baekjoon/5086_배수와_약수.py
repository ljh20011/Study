def sol(a, b):
    if b % a == 0:
        return "factor"
    if a % b == 0:
        return "multiple"
    else:
        return "neither"


while(1):
    a, b = map(int, input().split())
    if a == 0:
        break
    print(sol(a, b))
