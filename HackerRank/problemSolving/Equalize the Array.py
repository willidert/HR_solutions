def equalizeArray(arr):
    arrSet = set(arr)
    cont = 0
    for i in arrSet:
        x = arr.count(i)
        if x > cont:
            cont = x
    return len(arr) - cont

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)
