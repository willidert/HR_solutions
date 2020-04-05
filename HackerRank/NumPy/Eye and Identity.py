import numpy as np
n, m = map(int, input().split())
arr = str(np.eye(n, m, k=0))
arr = arr.replace('0', ' 0')
arr = arr.replace('1', ' 1')

print(arr)
