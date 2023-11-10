def temp(list, v):
    ans = 0
    for i in range(0, len(list)):
        if int(list[i]) == v:
            ans += 1
    return ans

n = int(input())
list = input().split()
v = int(input())
print(temp(list, v))
