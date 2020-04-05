import numpy as np

import numpy

def arrays(arr):
    arr = np.array(arr, float)
    return np.flip(arr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
