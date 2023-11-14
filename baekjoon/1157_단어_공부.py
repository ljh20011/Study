def sol(text):
    text = text.lower()
    temp = 0
    ans = 0
    alpha = [0]*26
    for i in range(len(text)):
        alpha[ord(text[i]) - 97] += 1

    for i in range(len(alpha)):
        if alpha[i] > temp:
            temp = alpha[i]
            ans = i

    alpha.sort()

    if alpha[-1] == alpha[-2]:
        return "?"
    return chr(ans + 65)

text = input()
print(sol(text))