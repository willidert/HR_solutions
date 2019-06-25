def findMedian(arr):
    meio = len(arr)//2
    arr.sort()
    return arr[meio]

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
