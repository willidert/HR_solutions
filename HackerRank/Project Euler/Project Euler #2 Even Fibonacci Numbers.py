t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    arr = [0, 1]
    soma = 0
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
        if arr[-1] > n:
            break
        if arr[-1] % 2 == 0:
            soma += arr[-1]
    print(soma)
