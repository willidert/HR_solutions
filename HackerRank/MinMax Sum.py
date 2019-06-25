def miniMaxSum(arr):
    menor = min(arr)
    maior = max(arr)
    arr.remove(menor)
    maxs = sum(arr)
    arr.append(menor)
    arr.remove(maior)
    mins = sum(arr)
    print(maxs, mins)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
