def sol(text):
    ans = [0] * 4
    for i in range(len(text)):
        if text[i] == "U":
            for j in range(i+1, len(text)):
                if text[j] == "C":
                    for k in range(j+1, len(text)):
                        if text[k] == "P":
                            for l in range(k+1, len(text)):
                                if text[l] == "C":
                                    print("I love UCPC")
                                    return
    print("I hate UCPC")
    return

text = input()
sol(text)