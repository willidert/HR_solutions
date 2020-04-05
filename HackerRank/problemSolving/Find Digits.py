def findDigits(n):
    strN = list(map(int, list(str(n))))
    cont = 0
    for i in strN:
        if i != 0 and n % i == 0:
            cont += 1
    return cont


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(result)
