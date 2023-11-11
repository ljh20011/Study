def sol(text):
    alpha = [-1] * 26
    print(alpha)
    for i in range(0, len(text)):
        if alpha[ord(text[i]) - 97] == -1:
            alpha[ord(text[i]) - 97] = i
    print(*alpha)

text = input()
sol(text)