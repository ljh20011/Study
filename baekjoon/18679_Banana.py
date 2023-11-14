def sol(m, dict):
    for i in range(m):
        k = int(input())
        sentence = input().split()
        for j in range(k):
            print(dict[sentence[j]], end=" ")
    return

n = int(input())
dict = {}
for i in range(n):
    text = input().split()
    dict[text[0]] = text[2]

m = int(input())
sol(m, dict)
