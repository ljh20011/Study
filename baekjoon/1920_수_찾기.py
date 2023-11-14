def sol(k, list_n, list_m, left, right):
    mid = (left + right) // 2
    if right < left:
        return 0
    if list_n[mid] == k:
        return 1
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

for k in range(0, m):
    print(sol(list_m[k], list_n, list_m, 0, n-1))