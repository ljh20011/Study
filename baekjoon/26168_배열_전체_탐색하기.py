
def lower_bound(k, list_n, idx, left, right):
    mid = (left + right) // 2
    if right < left:
        return int(mid)
    if list_n[mid] >= idx:
        right = mid - 1
        return lower_bound(k, list_n, idx, left, right)
    else :
        left = mid + 1
        return lower_bound(k, list_n, idx, left, right)
def upper_bound(k, list_n, idx, left, right):
    mid = (left + right) // 2
    if right < left:
        return int(mid)
    if list_n[mid] > idx:
        right = mid - 1
        return upper_bound(k, list_n, idx, left, right)
    else:
        left = mid + 1
        return upper_bound(k, list_n,idx, left, right)

def sol(a_list, k, idx, j=None):
    if k == 1:
        ans = len(a_list) - lower_bound(k, a_list, idx,0, len(a_list)-1) - 1
        return ans
    if k == 2:
        ans = len(a_list) - upper_bound(k, a_list, idx,0, len(a_list)-1) - 1
        return ans
    else:
        ans = upper_bound(k, a_list, j,0, len(a_list)-1) - lower_bound(k, a_list, idx,0, len(a_list)-1)
        return ans

n, m = map(int,input().split())
a_list = list(map(int, input().split()))
a_list.sort()
for i in range(m):
    order = list(map(int,input().split()))
    if len(order) == 3:
        print(sol(a_list, order[0], order[1], order[2]))
    else:
        print(sol(a_list, order[0], order[1]))
