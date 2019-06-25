def arrayManipulation(n, queries):
    arr = [0]*n
    for q in queries:
        for i in range(q[0]-1, q[1]):
            arr[i-1] += q[2]
    return max(arr)


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
