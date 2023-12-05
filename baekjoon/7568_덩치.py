def sol(height, weight, n):
    grade = [1] * n
    for i in range(n):
        for j in range(i+1, n):
            if (height[i] > height[j]) and (weight[i] > weight[j]):
                grade[j] += 1
            if (height[j] > height[i]) and (weight[j] > weight[i]):
                grade[i] += 1
    return grade

n = int(input())

height = [0] * n
weight = [0] * n

for i in range(n):
    height[i], weight[i] = map(int, input().split())


grade = sol(height, weight, n)
for i in range(n):
    print(grade[i])