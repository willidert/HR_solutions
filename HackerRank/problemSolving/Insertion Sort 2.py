def insertionSort2(n, arr):
    for i in range(1,n):
        temp=arr[i]
        j=i
        while j>0 and temp<arr[j-1]:
            arr[j] = arr[j-1]    
            j -= 1
        arr[j] = temp
        for _ in range(n):
            arr[_] = str(arr[_])
        print(' '.join(arr))
        for _ in range(n):
            arr[_] = int(arr[_])

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
