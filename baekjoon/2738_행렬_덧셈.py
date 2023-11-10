def sol(a, b, matrix_A, matrix_B):

    for i in range(a):
        for j in range(b):
            print(int(matrix_A[i][j]) + int(matrix_B[i][j]), end = " ")
        print("")

    return

a, b = map(int, input().split())
matrix_A = []
matrix_B = []

for i in range(a):  # A
    row = input().split()
    matrix_A.append(row)

for i in range(a):  # B
    row = input().split()
    matrix_B.append(row)

sol(a, b, matrix_A, matrix_B)
