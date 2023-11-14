def sol(text):
    ans = 0
    temp = []
    for i in range(len(text)):
        if ord(text[i]) < 68:
            temp.append(3)
        elif ord(text[i]) < 71:
            temp.append(4)
        elif ord(text[i]) < 74:
            temp.append(5)
        elif ord(text[i]) < 77:
            temp.append(6)
        elif ord(text[i]) < 80:
            temp.append(7)
        elif ord(text[i]) < 84:
            temp.append(8)
        elif ord(text[i]) < 87:
            temp.append(9)
        else:
            temp.append(10)

    for i in range(len(temp)):
        ans += temp[i]

    return ans

text = input()
print(sol(text))