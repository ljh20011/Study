def sol(text):
    ans = 0
    for i in range(len(text)):
        ans += int(text[i])
    return ans

text = input().split(",")
print(sol(text))