t = int(input().strip())

## Posso pressupor que a consulta está ordenada?


for _ in range(t):
    n = int(input().strip())
    arr = [0, 1]
    i = 2
    while True:
        arr.append(arr[i-1] + arr[i-2])
        i += 1
        if len(str(arr[-1])) == n:
            print(len(arr) - 1)
            break
