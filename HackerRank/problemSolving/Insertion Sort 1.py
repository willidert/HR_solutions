def insertionSort1(n, arr):
    for i in range(n-1,-1,-1):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]    
            j-=1
            for _ in range(len(arr)):
                arr[_] = str(arr[_])
            print(' '.join(arr))
            for _ in range(len(arr)):
                arr[_] = int(arr[_])
        if j != i - 1:
            arr[j+1] = temp
    for _ in range(len(arr)):
        arr[_] = str(arr[_])
    print(' '.join(arr))

            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
