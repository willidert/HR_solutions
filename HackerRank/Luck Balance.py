# Soma de todos subtraindo o menos importante

def luckBalance(k, contests):
    contests.sort()
    return contests

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)
