def sol(k, x):
    k.sort()
    cnt = 0
    left = 0
    right = len(k) - 1
    while(1):
        ans = k[left] + k[right]
        if left == right:
            break
        if ans == x:
            cnt += 1
            right -= 1
        elif ans > x:
            right -= 1
        else:
            left += 1
    return cnt

n = int(input())
k = list(map(int, input().split()))
x = int(input())

print(sol(k, x))