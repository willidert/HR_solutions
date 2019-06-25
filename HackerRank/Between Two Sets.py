#Repensar iso pq tá uma droga


def getTotalX(a, b):
    arr = list(range(1, b[0]+1))
    n = len(a)
    m = len(b)
    fatA = []
    cont = 0
    fator = False
    for i in arr:
        for j in a:
            if i % j == 0:
                fator = True
            else:
                fator = False
        if fator:
            fatA.append(i)
            
    fatB = []
    for i in fatA:
        for j in b:
            if j % i == 0:
                fator = True
            else:
                fator = False
    return cont


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
