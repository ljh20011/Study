def sol(text):
    for i in range(0, len(text), 10):
        print(text[i:i+10])

text = input()
sol(text)

