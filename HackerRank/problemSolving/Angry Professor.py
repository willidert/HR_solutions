def angryProfessor(k, a):
    cont = 0
    for i in a:
        if i <= 0:
            cont += 1
    if cont >= k:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)
