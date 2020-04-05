def minimumAbsoluteDifference(arr):
    if len(arr) != len(set(arr)):
        return 0
    arr.sort()
    return min(abs(arr[x] - arr[x+1]) for x in range(len(arr) - 1))


## greedy consiste em ordenar, organizar ou escolher
## por onde começar a execução seguindo algum critério bem definido


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
