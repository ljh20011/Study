def sol(text):
    text.sort()
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            return "no"
    return "yes"

text = input().split()
print(sol(text))