def sol(n):
    cnt = 1
    ans = 666
    while(1):
        if cnt == n:
            return ans
        ans += 1
        ans_list = str(ans)
        for i in range(0, len(ans_list)-2):
            if cnt == n:
                return ans
            if (ans_list[i] == "6" and ans_list[i + 1] == "6") and ans_list[i + 2] == "6":
                cnt += 1
                break

n = int(input())

print(sol(n))
