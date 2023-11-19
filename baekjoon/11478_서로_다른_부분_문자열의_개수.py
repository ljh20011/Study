def sol(s):
    ans = set()
    for i in range(1, len(s)+1): # 문자열의 길이
        for j in range(0,len(s)): # 시작점
            ans.add(s[j:j+i])
    return len(ans)


s = input()
print(sol(s))

