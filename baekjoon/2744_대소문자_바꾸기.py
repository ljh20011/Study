def sol(text):
    for i in range(0, len(text)):
        if ord(text[i]) > 96: # lower
            print(chr(ord(text[i])-32), end = "")
        else : # upper
            print(chr(ord(text[i])+32), end = "")
    return

text = input()
sol(text)