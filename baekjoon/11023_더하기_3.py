def sol(list):
    ans = 0
    for i in range(0, len(list)):
        ans += int(list[i])
    return ans

list = input().split()
print(sol(list))
