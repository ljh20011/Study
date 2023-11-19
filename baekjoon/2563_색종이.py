def sol(paper, left = -1, down = -1):
    if down < 0:
        cnt = 0
        for i in paper:
            cnt += sum(i)
        return cnt

    for k in range(10):
        for j in range(10):
            paper[down + k][left + j] = 1

    return paper

paper = [[0]*101 for i in range(101)]

n = int(input())
for i in range(n):
    left, down = map(int, input().split())
    paper = sol(paper, left, down)

print(sol(paper))


