def sol(k, list_n, list_m, left, right):
    mid = (left + right) // 2
    if right < left:
        return 0
    if list_n[mid] == k:
        return mid
    if list_n[mid] > k:
        right = mid - 1
        return sol(k, list_n, list_m, left, right)
    if list_n[mid] < k :
        left = mid + 1
        return sol(k, list_n, list_m, left, right)

n = int(input())
list_n = list(map(int, input().split()))
list_n.sort()

m = int(input())
list_m = list(map(int, input().split()))
ans = [0] * m
for k in range(0, m):
    left_idx = (sol(list_m[k] - 1, list_n, list_m, 0, n-1))
    right_idx = (sol(list_m[k] + 1, list_n, list_m, 0, n-1))

    ans[k] = right_idx - left_idx - 1
    print(ans)
print(*ans)