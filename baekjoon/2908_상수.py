def sol(text):
    a = int(text[0][::-1])
    b = int(text[1][::-1])
    if a >= b:
        return a
    else:
        return b

text = input().split()
print(sol(text))