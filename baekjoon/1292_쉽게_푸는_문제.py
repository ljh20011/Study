def sol(list, v):
    for i in range(0, len(list)):
        if int(list[i]) < v:
            print(list[i], end= " ")

n, x = input().split()

list = input().split()
sol(list, int(x))