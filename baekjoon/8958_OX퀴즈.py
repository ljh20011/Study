def sol(text):
    text.sort()
    if len(text) % 2 == 1:
        if (text[(len(text) - 1) // 2] == "A"):
            return "A"
        else :
            return "B"
    else :
        if text[len(text) // 2] == "A":
            return "A"
        elif text[len(text) // 2 - 1] == "B":
            return "B"
        else :
            return "Tie"

n = int(input())
text = list(input())
print(sol(text))