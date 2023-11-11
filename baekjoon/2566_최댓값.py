def sol(matrix):
    ans = -1
    for i in range(9):
        for j in range(9):
            if ans < matrix[i][j]:
                ans = matrix[i][j]
                location = [i,j]
    print(ans)
    print(location[0] + 1, location[1]+1)

matrix = []
for i in range(9):
    matrix.append(list(map(int,input().split())))

sol(matrix)