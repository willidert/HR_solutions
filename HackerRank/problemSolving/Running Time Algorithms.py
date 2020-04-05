def runningTime(arr):
    shift = 0
    for i in range(1, len(arr)):
        j = i-1
        temp = arr[i]
        while (j >= 0) and (arr[j] > temp):
           arr[j+1] = arr[j]
           j -= 1
           shift+=1
        arr[j+1] = temp
    return shift

if __name__ =='__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    print(result)
