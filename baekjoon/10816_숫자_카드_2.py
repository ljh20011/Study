def sol(s, k):
    ans = [0] * len(k)
    for i in s:
        for j in range(len(k)):
            if i == k[j]:
                ans[j] += 1
    return ans

n = int(input())
s = input().split()

m = int(input())
k = input().split()

print(sol(s, k))
