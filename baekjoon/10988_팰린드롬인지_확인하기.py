def sol(text):
    for i in range(0, (len(text) // 2)):
        if text[i] != text[-1 * (i+1)]:
            return 0
    return 1

text = input()
print(sol(text))