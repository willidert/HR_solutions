if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    b = [0 for _ in range(len(a))]

    for i in range(len(a)):
        b[i-d] = a[i]
    for num in b:
        print(num, end=' ')
