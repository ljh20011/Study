def sol(text):
    for j in range(len(text[1])):
        print(text[1][j] * int(text[0]), end ="")
    print("")
    return

n = int(input())

for i in range(n):
    text = input().split()
    sol(text)