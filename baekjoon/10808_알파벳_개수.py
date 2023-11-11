def sol(text):
    alpha = [0] * 26
    for i in range(0, len(text)):
        alpha[ord(text[i]) - 97] += 1
    print(*alpha)

text = input()
sol(text)