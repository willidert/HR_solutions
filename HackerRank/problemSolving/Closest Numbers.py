def closestNumbers(arr):
    arr.sort()
    res = []
    dif = arr[1] - arr[0]
    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i])  < dif:
            dif = arr[i+1] - arr[i]
    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i]) == dif:
            print(arr[i], arr[i+1])
            res.append(arr[i])
            res.append(arr[i+1])
    return res


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
