import itertools


def pairs(k, arr):
    conj = itertools.combinations(arr, 2)
    cont = 0
    for i in conj:
        if max(i) - min(i) == k:
            cont += 1
    return cont


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)
