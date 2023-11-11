def sol(num):
    ans = 0
    for i in range(0, len(num)):
        ans += int(num[i])
    return ans

n = int(input())
num = input()
print(sol(num))

