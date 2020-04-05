import numpy as np

n, m  = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

arr = np.array(arr)

print(np.transpose(arr))
print(arr.flatten())
