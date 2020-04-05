def saveThePrisoner(n, m, s):
    doces = m%n - 1
    pris = s
    if m%n == 0:
        if pris == 1:
            pris = n
        else:
            pris -= 1
    elif pris + doces > n:
        pris = doces - (n - pris)
    else:
        pris += doces
        
    return pris

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        print(result)
