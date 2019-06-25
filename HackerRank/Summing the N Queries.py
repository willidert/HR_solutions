def summingSeries(n):
    arr = []
    cont = 1
    while len(arr) != n:
        arr.append(cont**2 - (cont - 1) ** 2)
        cont += 1
    return sum(arr)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        print(result)
