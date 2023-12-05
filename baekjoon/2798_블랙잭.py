def sol(m, card):
    card.sort()
    ans = m
    for i in range(len(card)):
        a = card[i]
        for j in range(i+1, len(card)):
            b = card[j]
            for k in range(j+1, len(card)):
                c = card[k]
                print(i, j, k)
                if m - (a + b + c) < 0 :
                    break
                if m - (a + b + c) <= ans :
                    ans = m - (a + b + c)
    return m - ans

n, m = map(int, input().split())
card = list(map(int, input().split()))

print(sol(m, card))
