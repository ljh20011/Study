def sol(text):
    ans = []
    for i in range(len(text)):
        if ord(text[i]) - 3 < 65  :
            ans.append(chr(90 - (67 - ord(text[i]))))
        else :
            ans.append(chr(ord(text[i]) - 3))
    ans = ''.join(ans)
    return ans

text = input()
print(sol(text))