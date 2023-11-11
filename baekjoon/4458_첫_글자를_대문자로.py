def sol(text):
    ans = text[0].upper() + text[1:]
    return ans

n = int(input())

for i in range(n):
    text = input()
    print(sol(text))