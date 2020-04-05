from itertools import combinations_with_replacement as comb_replace

arr, n = input().split()
n = int(n)
arr = list(arr)
arr.sort()
arr = ''.join(arr)
vetor = comb_replace(arr, n)

for i in vetor:
    print(''.join(i))
