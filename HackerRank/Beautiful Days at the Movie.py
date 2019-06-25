def beautifulDays(i, j, k):
    cont = 0
    for i in range(i, j+1):
        aux = list(str(i))
        aux.reverse()
        aux = int(''.join(aux))
        aux = i - aux
        if aux < 0:
            aux *= -1
        if aux % k == 0:
            cont += 1
    return cont

if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)
