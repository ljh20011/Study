def sol(text):
    return(text[0] + text[-1])

n = int(input())

for i in range(n):
    text = input()
    print(sol(text))

