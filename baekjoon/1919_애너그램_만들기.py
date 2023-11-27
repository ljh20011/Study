def sol(a, b):
    a_alpha = [0] * 26
    b_alpha = [0] * 26
    cnt = 0
    for i in range(len(a)):
        a_alpha[ord(a[i]) - 97] += 1
    for i in range(len(b)):
        b_alpha[ord(b[i]) - 97] += 1
    for i in range(len(a_alpha)):
        cnt += abs(a_alpha[i] - b_alpha[i])
    return cnt

a = input()
b = input()

print(sol(a, b))