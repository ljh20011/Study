def sol(text):
    alpha = [0] * 26
    for i in range(0, len(text)):
        alpha[ord(text[i]) - 97] += 1
    print(*alpha)
list1 = [1,2]
list2 = [2, 1]
print(list1 * list2)
text = input()
sol(text)
