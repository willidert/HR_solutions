import numpy as np

n, m, p = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(list(map(int, input().split())))
for i in range(m):
    arr2.append(list(map(int, input().split())))

print(np.concatenate((arr1, arr2)))
