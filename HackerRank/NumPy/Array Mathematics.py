import numpy as np
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arrA = np.array(arr)
arr = [list(map(int, input().split())) for i in range(n)]
arrB = np.array(arr)
print(arrA + arrB)
print(arrA - arrB)
print(arrA * arrB)
print(arrA // arrB)
print(arrA % arrB)
print(arrA ** arrB)
