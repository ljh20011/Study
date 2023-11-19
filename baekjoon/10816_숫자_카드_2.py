def lower_bound(k, list_n, list_m, left, right):
    mid = (left + right) // 2
    if right < left:
        return int(mid)
    if list_n[mid] >= k:
        right = mid - 1
        return lower_bound(k, list_n, list_m, left, right)
    else :
        left = mid + 1
        return lower_bound(k, list_n, list_m, left, right)
def upper_bound(k, list_n, list_m, left, right):
    mid = (left + right) // 2
    if right < left:
        return int(mid)
    if list_n[mid] > k:
        right = mid - 1
        return upper_bound(k, list_n, list_m, left, right)
    else:
        left = mid + 1
        return upper_bound(k, list_n, list_m, left, right)

n = int(input())
s = list(map(int, input().split()))
s.sort()

m = int(input())
k = list(map(int, input().split()))

ans = []
for i in k:
    ans.append(upper_bound(i, s, k, 0, n-1) - lower_bound(i, s, k, 0, n-1))
print(*ans)
