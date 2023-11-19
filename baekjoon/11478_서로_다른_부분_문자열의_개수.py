import numpy as np
def sol(s):
    ans = set()
    for i in range(1, len(s)+1): # 문자열의 길이
        for j in range(0,len(s)): # 시작점
            ans.add(s[j:j+i])
    return len(ans)

array1 = np.arange(10)
array4 = array1.reshape(-1, 2)
print('array4:\n', array4)

array5 = array1.reshape(2, -1)
print(len(array5))
print('array5:\n', array5)

s = input()
print(sol(s))
